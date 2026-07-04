"""Decorators - Function Enhancement Decorators.

Provides decorators for common function behaviors.
"""

import functools
import time
from typing import Callable, Any


def timed(func: Callable) -> Callable:
    """Decorator to measure function execution time.

    Args:
        func: Function to decorate.

    Returns:
        Decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"[Timer] {func.__name__} took {duration:.4f}s")
        return result

    return wrapper


def requires_internet(func: Callable) -> Callable:
    """Decorator to check internet connectivity.

    Args:
        func: Function to decorate.

    Returns:
        Decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            import requests
            requests.get('https://www.google.com', timeout=2)
        except Exception:
            raise RuntimeError(f"{func.__name__} requires internet connection")

        return func(*args, **kwargs)

    return wrapper
