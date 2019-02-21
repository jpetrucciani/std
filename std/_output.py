from ._pipes import stdout


def puts(s, fd=std_out, newline="\n"):
    line = f"{s}{newline}"
    return print(line, end=newline, file=fd)
