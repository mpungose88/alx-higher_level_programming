#!/usr/bin/python3

if_name_ == "_main_":
"""Print names that are defined by hidden."""

names = dir(hidden)
for name in names:
    if name[:2]!= "_":
        print(name)
