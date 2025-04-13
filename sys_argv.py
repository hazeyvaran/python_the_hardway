# the sys.argv is just a list of items from the command line.
# since de define all items between 1 and :, it will spit out everything which was included with it to begin with.

# # 1. Basic example
# import sys
#
# print("script name", sys.argv[0]) # then name of the script
# print("arguments:", sys.argv[1:]) # all arguments, except for script name


# dont forget sys.argc[0] is always the name of the script. regardless of that variable being initialized. done automat.
# if there is less than 3 arguments are given = script name and 2 more arguments. it will only print first text.
# sys.exit(1) exits the program and the 1 defines an error occured.

# 2. Accessing individual arguments
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py requires more than 1 argument <argv1> <argv2>")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(f"first argument: {arg1}")
print(f"second argument: {arg2}")








