#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models
from models.city import city


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            cities = models.storage.all(City)
            cities_in_state = []
            for city in cities.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
