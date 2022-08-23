#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')+1):
            i = chr(ord(i) - ord('a') + ord('A'))
            print("{}".format(i), end='')
    print()
