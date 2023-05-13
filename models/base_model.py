"""Defines the Base class for all classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes and methods

    Attributes:
        id (str): the uuid of the instance
        created_at (datetime): current datetime when instance was created
        updated_at (datetime): datetime when instance was last updated
    """

    id = str(uuid.uuid4())
    create_at = datetime.now()
    updated_at = datetime.now()


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
        self_dict[__class__] = type(self).__name__
        if "created_at" in self_dict.keys():
            self_dict["created_at"] = self.created_at.isoformat()

        if "updated_at" in self_dict.keys():
            self_dict["updated_at"] = self.updated_at.isoformat()
