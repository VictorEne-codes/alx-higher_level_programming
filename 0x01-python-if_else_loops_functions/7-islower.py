#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc >= ord('a') and asc <= ord('z'):
        return True
    else:
        return False
