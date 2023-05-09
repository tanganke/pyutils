R"""
misc usefull functions and classes.
"""
from . import collections, logging, path
from .args import *
from .logging import titled_log
from .timeit import *


def first(iterable):
    return next(iter(iterable))
