#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from datetime import datetime
import os
import time
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        momentSav = datetime.now()
        inst1 = BaseModel()
        momentSav2 = datetime.now()

        

        self.assertIsInstance(inst1.created_at, datetime)
        self.assertLess(inst1.created_at, momentSav2)
        self.assertGreater(inst1.created_at, momentSav)
        
        self.assertGreater(inst1.updated_at, momentSav)
        
        
        self.assertIsInstance(inst1.updated_at, datetime)
        self.assertGreater(inst1.updated_at, momentSav)
		self.assertIsInstance(inst1.id, str)
        self.assertTrue(len(inst1.id) > 0)
        self.assertTrue('BaseModel.' + inst1.id in storage.all().keys())
		inst1.save()
        self.assertIsInstance(inst1.updated_at, datetime)
        self.assertLess(inst1.updated_at, momentSav2)
        self.assertGreater(inst1.updated_at, momentSav2)
        del inst1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        inst2 = BaseModel(**test_dict)

        self.assertIsInstance(inst2.id, str)
        self.assertTrue(len(inst2.id) > 0)
        self.assertTrue(inst2.id == test_dict['id'])
        
        self.assertIsInstance(inst2.created_at, datetime)
        self.assertTrue(inst2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(inst2.updated_at, datetime)
        self.assertTrue(inst2.updated_at.isoformat('T') == test_dict['updated_at'])
        inst2.save()
        self.assertGreater(inst2.updated_at, inst2.created_at)
        del inst2
