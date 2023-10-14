#!/usr/bin/python3
"""The review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review inherited from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
