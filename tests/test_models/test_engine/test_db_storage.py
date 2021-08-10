#!/usr/bin/python3
""" Unittests for db_storage """
import unittest
import MySQLdb
import os
from models.engine.db_storage import DBStorage
from models.user import User


class TestDBStorage(unittest.TestCase):
    """Tests for SQLAlchemy storage method."""

    db = MySQLdb.connect(host="localhost", user='hbnb_test',
                         passwd='hbnb_test_pwd', db='hbnb_test_db')
    cur = db.cursor()
    os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
    os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
    os.environ['HBNB_MYSQL_HOST'] = 'localhost'
    os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
    os.environ['HBNB_TYPE_STORAGE'] = 'db'
    os.environ['HBNB_ENV'] = 'test'

    @classmethod
    def setUpClass(cls):
        """setup for funsies."""
        cls.user = User()
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"
        cls.user.email = "john@mqil.com"
        cls.storage = DBStorage()

    def test_all(self):
        """tests if all works in File Storage"""
        pass
