#!/usr/bin/python3
"""Defines the Review class"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review

    Attributes:
        place_id (str): empty string
        user_id (str): empty string
        text (str): empty string
    """
    place_id = ""
    user_id = ""
    text = ""
