#!/usr/bin/python3
"""Defines the User class"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Defines a user

    Attributes:
        email (str) - empty string
        password (str) - empty string
        first_name (str) - empty string
        last_name (str) - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
