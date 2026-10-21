"""Minimal lab application package for ANU experiments."""

__version__ = "0.1.0"


def greet(name: str = "world") -> str:
    """Return a greeting — seed unit for the test matrix."""
    return f"Hello, {name}!"

from .ping import ping  # noqa: F401
