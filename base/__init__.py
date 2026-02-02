"""
Base package for shared test utilities.

Exposes the main `BaseTest` class and `logger` used across the test suite.
"""

from .base_test import BaseTest, logger

__all__ = ["BaseTest", "logger"]
