#!/usr/bin/python3
""" Unittests for db_storage """
import unittest
import os
import MySQLdb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import os


class TestDBStorage(unittest.TestCase):
    """Tests for SQLAlchemy storage method."""

    db = MySQLdb.connect(host="127.0.0.1", user='hbnb_test',
                         passwd='hbnb_test_pwd', db='hbnb_test_db')
    cur = db.cursor()
    os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
    os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
    os.environ['HBNB_MYSQL_HOST'] = '127.0.0.1'
    os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
    os.environ['HBNB_TYPE_STORAGE'] = 'db'
    os.environ['HBNB_ENV'] = 'test'

    @classmethod
    def setUpClass(cls):
        """setup for funsies."""
        cls.user = User()
        cls.user.first_name = "Nate"
        cls.user.last_name = "KittyCat"
        cls.user.email = "murderface@bird.com"
        cls.storage = DBStorage()

    def test_db_basic(self):
        pass

    def test_all(self):
        """tests if all works in File Storage"""
        pass
