#!/usr/bin/python3
"""Defines review class"""

from models.base_model import BaseModel

class State(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""
