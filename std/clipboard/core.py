import sys

if sys.platform == "darwin":
    from std.clipboard.darwin import copy, paste

elif sys.platform == "win32":
    try:
        from std.clipboard.win import copy, paste
    except ImportError:
        from std.clipboard.tkinter import copy, paste

elif sys.platform == "cli":
    from std.clipboard.cli import copy, paste

else:
    from std.clipboard.x11 import copy, paste
