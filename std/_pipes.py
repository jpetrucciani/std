from sys import stdin, stderr, stdout
from typing import IO


def puts(s: str, fd: IO = stdout, newline: str = "\n") -> None:
    """puts a string into the file descriptor"""
    line = "{s}{newline}".format(s=s, newline=newline)
    return print(line, end=newline, file=fd)


def piped_in(fd: IO = stdin) -> str:
    with fd as in_fd:
        # TTY is only way to detect if stdin contains data
        if not in_fd.isatty():
            return in_fd.read()
        else:
            return ""
