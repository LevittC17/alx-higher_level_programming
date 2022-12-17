#!/usr/bin/python3
def uppercase(str):
    for characters in str:
        if ord(characters) > 96 and ord(characters) < 123:
            characters = chr(ord(characters) - 32)
        print('{:s}'.format(characters), end="")
    print('\n', end="")
