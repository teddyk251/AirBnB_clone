#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """test BaseModel"""

    def test_init_con(self):
        """test BaseModel"""
        event_time = datetime.now()
        userIns = User()

        self.assertIsInstance(userIns.id, str)
        self.assertTrue('User.' + userIns.id in storage.all().keys())
        self.assertIsInstance(userIns.created_at, datetime)
        self.assertIsInstance(userIns.updated_at, datetime)
        userIns.save()
        self.assertIsInstance(userIns.updated_at, datetime)

        del userIns
        
    def test_dict(self):
        """test dict"""
        test_dict = {'updated_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')
                     , 'id': 'l3142b62-03fa-jaae-37de-830705d8313z', 'created_at': datetime(2021, 13, 22, 12, 30, 00, 618421).isoformat('T')}
        userIns2 = User(**test_dict)

        self.assertIsInstance(userIns2.id, str)
        self.assertTrue(len(userIns2.id) > 0)
		self.assertTrue(userIns2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(userIns2.updated_at, datetime)
        self.assertTrue(userIns2.updated_at.isoformat('T') == test_dict['updated_at'])
        self.assertTrue(userIns2.id == test_dict['id'])
        
        self.assertIsInstance(userIns2.created_at, datetime)
        
        userIns2.save()
        del userIns2

    def test_attr(self):
        """testing attribute"""
        userIns3 = User()

        self.assertTrue(hasattr(userIns3, "email"))
        self.assertTrue(hasattr(userIns3, "password"))
        self.assertTrue(hasattr(userIns3, "first_name"))
        self.assertTrue(hasattr(userIns3, "last_name"))

        self.assertIsInstance(userIns3.email, str)
        self.assertIsInstance(userIns3.password, str)
        self.assertIsInstance(userIns3.first_name, str)
        self.assertIsInstance(userIns3.last_name, str)

