"""
This module holds wrappers and utils related to deprecation
"""

from functools import wraps

def deprecated(func):
    """ indicated the wrapped function is deprecated """

    @wraps(func)
    def wrapper(*args, **kwds):
        """ Print/Log a deprecation message """
        logger.debug("Deprecated: %s is deprecated", func.__name__)
        return func(*args, **kwds)

    return wrapper
