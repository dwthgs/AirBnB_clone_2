#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_type != "db":
    @property
    def cities(self):
        """ getter attribute cities that returns
        list of City instances with state_id equals
        to the current State.id """
        self.state_id = State.id
        li = []
        all_city = models.storage.all(city)
        for val in all_city.values():
            if val.state_id == self.id:
                li.append(val)
        return li
