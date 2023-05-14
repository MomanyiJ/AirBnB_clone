#!/usr/bin/python3
"""Defines the Base class for all classes
"""

import uuid
import copy
from datetime import datetime
from datetime import date


class BaseModel:
    """Defines all common attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """Initialises the instance

        Attributes:
            id (str): the uuid of the instance
            created_at (datetime): current datetime when instance was created
            updated_at (datetime): datetime when instance was last updated
        """

        if (len(kwargs) > 0):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value,
                                                     "%Y-%m-%dT%H:%M:%S.%f"))

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    def __str__(self):
        """Provides the string output for the object
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                self.__dict__)

    def save(self):
        """Updates the updated_at attribute with tehe current datetime
        """

        self.updated_at = datetime.now()


    def to_dict(self):
        """Returns all the key-value pairs of __dict__ of the instance
        """

        self_dict = self.__dict__
        self_dict["__class__"] = type(self).__name__

        #TODO: the deepcopy function doesn't seem to work. created-updated_at
        # are converted to the ISO strings. Maybe another solution??
        create_date = copy.deepcopy(self.created_at)
        self_dict["created_at"] = create_date.isoformat()

        update_date = copy.deepcopy(self.updated_at)
        self_dict["updated_at"] = update_date.isoformat()

        return self_dict
