#!/usr/bin/python3
""" State Module for HBNB project """
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
        for city in storage.all(City).values():
            if isinstance(city, City) and city.state_id == self.id:
                city_list.append(city)
        return city_list
