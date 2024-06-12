#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter attribute to returns the list of City objects."""
        from models import storage
        from models.city import City
        city_list = []
        result = []
        total = storage.all()

        for city in total:
            new = city.replace('.', ' ')
            new = shlex.split(new)
            if new[0] == 'City':
                city_list.append(total[city])
        for city_name in city_list:
            if (city_name.state_id == self.id):
                result.append(city_name)
        return result
