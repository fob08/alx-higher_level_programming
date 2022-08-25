#!/usr/bin/python3
if __name__ =="__main__":
    import sys
    add = 0
    size = len(sys.argv)
    if size > 1:
        for i in range(1,size):
            add += (int(sys.argv[i]))
    print("{:d}".format(add))
