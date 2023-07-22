R"""
misc usefull functions and classes.
"""
from typing import Iterable
import importlib

from . import collections, logging, path
from .args import *
from .logging import TitledLog, titled_log
from .timeit import *


def first(iterable: Iterable):
    R"""Returns the first element of `iterable`.

    Examples:

        >>> first_batch = first(data_loader)

    Args:
        iterable (Iterable): _description_

    Returns:
        Any: _description_
    """
    return next(iter(iterable))


def import_object(module_name: str, object_name: str):
    module = importlib.import_module(module_name)
    obj = getattr(module, object_name)
    return obj
