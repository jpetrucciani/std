""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from std.clipboard.base import Pywin32NotFound
from typing import Any

try:
    import win32clipboard as clip
    import win32con
except ImportError as why:
    raise Pywin32NotFound


def copy(string: str, **kwargs: Any) -> None:
    """Copy given string into system clipboard."""

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardData(win32con.CF_UNICODETEXT, string)
    clip.CloseClipboard()

    return


def paste(**kwargs: Any) -> str:
    """Returns system clipboard contents."""

    clip.OpenClipboard()
    d = clip.GetClipboardData(win32con.CF_UNICODETEXT)
    clip.CloseClipboard()
    return d
