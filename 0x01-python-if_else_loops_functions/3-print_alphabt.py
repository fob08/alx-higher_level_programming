#!/usr/bin/python3
for p in range(ord('a'), ord('z')+1):
    if p is not (ord('q')) and p is not (ord('e')):
        print("{}".format(chr(p)), end='')
