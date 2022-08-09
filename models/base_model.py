#!/bin/usr/python3
"""file contains basemodel class"""
from datetime import datetime
from models import storage
import uuid


class BaseModel():
    """base model for AirBnB Clone"""

    def __init__(self, *args, **kwargs):
        """initialization"""
        if(bool(kwargs)):
            for key in kwargs.keys():
                if(key != '__class__'):
                    setattr(self, key, kwargs[key])
                    self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f') 
                    self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
			
    def __str__(self):
        """str"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """updated_at with current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dictionary"""
        self_dictionary = dict(self.__dict__)
        self_dictionary['__class__'] = self.__class__.__name__
        self_dictionary['created_at'] = datetime.isoformat(self.created_at)
        self_dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return self_dictionary
