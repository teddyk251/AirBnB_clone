#!/usr/bin/python3
"""File Storage"""

from os.path import exists
import json

class FileStorage:
    """for FileStorage"""

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets key """
        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """serialize to JSON file"""
        temp = dict()
        for keys in self.__objects.keys():
            temp[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, mode='w') as jsonfile:
            json.dump(temp, jsonfile)

    def reload(self):
        """deserializes JSON file to __objects"""
        from ..base_model import BaseModel
        from ..amenity import Amenity
        from ..place import Place
        from ..state import State
        from ..city import City
        from ..user import User
        from ..review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as jsonfile:
                reloaded_dict = json.load(jsonfile)
            for keys in reloaded_dict.keys():
                if reloaded_dict[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**reloaded_dict[keys])
                elif reloaded_dict[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**reloaded_dict[keys])
