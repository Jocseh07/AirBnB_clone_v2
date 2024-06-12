#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter attribute to returns the list of City objects."""
        city_list = []
        result = []
        total = storage.all()

        for city in total:
            city = city.replace('.', ' ')
            city = city.split()
            if city[0] == 'City':
                city_list.append(total[city])
        for name in city_list:
            if (name.state_id == self.id):
                result.append(name)
        return result
