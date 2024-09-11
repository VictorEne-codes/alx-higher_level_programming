#!/usr/bin/python3
ch = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - ch)), end="")
    ch = 32 if ch == 0 else 0
