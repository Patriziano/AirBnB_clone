#!/usr/bin/python3
"""The Amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherited from the BaseModel to show the amenities each location has
    """
    name = ""
