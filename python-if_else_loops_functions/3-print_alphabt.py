#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    print("{}".format(chr(x)), end='') if chr(x) not in 'qe' else None
