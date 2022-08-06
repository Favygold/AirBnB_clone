#!/usr/bin/python3
"""Defines the City class"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Defines a city

    Attributes:
        state_id (str): empty string. This will be the State.id
        name (str): empty string
    """
    state_id = ""
    name = ""
