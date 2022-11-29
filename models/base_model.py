#!/usr/bin/python3
'''Defines `BaseModel` class'''

import uuid
from datetime import datetime


class BaseModel:
    '''Defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''Initializes a new instance
        '''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value


    def __str__(self):
        '''String representation of our instance
        '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        '''updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of
        __dict__ of the instance
        '''
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
