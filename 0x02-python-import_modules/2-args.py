#!/usr/bin/python3

import sys

# ensure the program is executed from the main script
if __name__ == "__main__":
    args = sys.argv[1:]
    # check the length of arguments
    num_args = len(args)
    # check if arguments = null
    if num_args == 0:
        print("0 arguments.")
    # check if arguments = 1
    elif num_args == 1:
        print("1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{num_args} arguments:")

        # iterate through the args list
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
