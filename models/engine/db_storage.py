#!/usr/bin/python3
"""New engine."""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Create new storage."""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects depending on class."""

        dictionary = {}
        if cls:
            all = self.__session.query(cls)
            for one in all:
                key = "{}.{}".format(type(one).__name__, one.id)
                dictionary[key] = one
        else:
            check = [User, State, City, Amenity, Place, Review]
            for one in check:
                all = self.__session.query(one)
                for el in one:
                    key = "{}.{}".format(type(el).__name__, el.id)
                    dictionary[key] = el
        return (dictionary)

    def new(self, obj):
        """Add an object to the session."""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the session."""
        self.__session.commit()

    def delete(self, obj=None):
        """commit all changes to the session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload."""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """Call remove method."""
        self.__session.close()
