#!/usr/bin/python3
"""Create a unique FileStorage instance for the application"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
