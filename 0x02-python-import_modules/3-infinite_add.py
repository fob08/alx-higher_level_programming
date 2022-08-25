#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv
    userinput = (argv[1:])
    add = 0
    size = len(userinput)
    for i in range(1,size):
        add+=int(userinput[i])

