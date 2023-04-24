R"""
misc usefull functions and classes.
"""
from . import collections, logging, path
from .args import *
from .timeit import *


def first(iterable):
    return next(iter(iterable))
