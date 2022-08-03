#!/usr/bin/python3
"""Defines the BaseModel class"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Defines public instance variables

        Args:
            args (any): unused
            kwargs (dict): key/value pairs of instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        dtformat = "%Y-%m-%dT%H:%M:%S.%f"  # datetime format

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.strptime(value, dtformat)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def __str__(self):
        """Prints/Returns string representation of a BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute ``updated_at``
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of BaseModel instance.

        This includes key/value pair ``__class__`` representing
        the name of the class"""
        dic = self.__dict__.copy()
        # Convert to string object in ISO format
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        dic['__class__'] = self.__class__.__name__  # added object's class name
        return dic
