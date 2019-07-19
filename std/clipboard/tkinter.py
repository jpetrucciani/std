"""
Copy + Paste in Windows, Linux or Mac

found @ http://code.activestate.com/recipes/150115/
"""

from std.clipboard.base import TkinterNotFound
from typing import Any

try:
    from Tkinter import Tk
except ImportError as why:
    raise TkinterNotFound


def copy(string: str, **kwargs: Any) -> None:
    """Copy given string into system clipboard."""
    window = Tk()
    window.withdraw()
    window.clipboard_clear()
    window.clipboard_append(string)
    window.destroy()
    return


def paste(**kwargs: Any) -> str:
    """Returns system clipboard contents."""
    window = Tk()
    window.withdraw()
    d = window.selection_get(selection="CLIPBOARD")
    return d
