import sys


def piped_in(fd=sys.stdin):
    with fd as stdin:
        # TTY is only way to detect if stdin contains data
        if not stdin.isatty():
            return stdin.read()
        else:
            return None
