#!/usr/bin/python3
"""Module for the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Parent class that defines all common attributes/methods for other classesi
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor that initializes each instances of the class
        Args:
            args: tuple that contains all arguments
            kwargs: a dictionary that contains all arguments by key/value
            If `kwargs` is provided, it creates an instance
            from the dictionary representation.
        """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                # do not add __class__ as part of the attributes
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        It returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        class_name = self.__class__.__name__
        dict_ = self.__dict__.copy()
        dict_['__class__'] = class_name
        dict_['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_

    def __str__(self):
        """
        Prints all the string representation of the data structures
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
