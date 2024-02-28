#!/usr/bin/python3
"""This module creates a unique FileStorage instance for the application
"""
# models/__init__.py
from .engine.file_storage import FileStorage
from .base_model import BaseModel

storage = FileStorage()
storage.reload()
