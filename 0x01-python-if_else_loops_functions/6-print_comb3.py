#!/usr/bin/python3
for i in range(0,10):
    for i+1 in range(0,10):
        print(", ".join("{}{}".format(i, i+1)))
    i++
