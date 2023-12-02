#!/usr/bin/python3

def magic_calculatio(a,b):
    """Match bytecode provided that is provided by Holberton School"""
    if a < b:
        c =add(a, b)
        for i in range(4,6):
            c = add(c, i)

        Return(c)

    else:
        return(sub(a, b))
