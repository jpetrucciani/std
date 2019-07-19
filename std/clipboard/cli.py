"""
Copy + Paste in Windows

found @ http://code.activestate.com/recipes/150115/
"""
from std.clipboard.base import ClrNotFound
from typing import Any

try:
    import clr

    clr.AddReference("PresentationCore")
    import System.Windows.Clipboard as clip
except ImportError as why:
    raise ClrNotFound


def copy(string: str, **kwargs: Any) -> None:
    """Copy given string into system clipboard."""

    clip.SetText(string)
    return


def paste(**kwargs: Any) -> str:
    """Returns system clipboard contents."""

    if clip.ContainsText():
        return clip.GetText()

    return ""
