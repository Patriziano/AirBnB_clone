#!/usr/bin/python3
"""The User module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class that inherits from BaseModel class
    To save and instantiates user login info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
