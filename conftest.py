"""
Pytest configuration file
"""

import pytest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )


@pytest.fixture(scope="session")
def base_url():
    """Return base URL for tests"""
    return "https://gamerpc-admin-git-testing-decimal-pro-team.vercel.app"


@pytest.fixture(scope="session")
def admin_credentials():
    """Return admin credentials"""
    return {
        "email": "admin@gmail.com",
        "password": "Bmr@1234"
    }
