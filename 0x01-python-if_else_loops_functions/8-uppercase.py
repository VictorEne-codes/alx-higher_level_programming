#!/usr/bin/python3
def uppercase(str):
    res = ''
    for i in str:
        asc = ord(i)
        if asc >= ord('a') and asc <= ord('z'):
            res += chr(asc - 32)
        else:
            res += i
    print(res)
