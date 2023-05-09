import logging
from typing import Any, Callable

from .rich import *


def titled_log(
    title: str,
    msg: Any,
    title_width: int = 50,
    log_fn: Callable = print,
):
    log_fn(f"{title:=^{title_width}}")
    log_fn(msg)
    log_fn(f"{'':=^{title_width}}")
