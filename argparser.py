import sys
#
# print("script name:", sys.argv[0])
# print("argument:", sys.argv[1:])


####################################

#accessing individual arguments
if len(sys.argv) < 3:
    print("usage: python script <arg1> <arg2>")
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(f"first argument: {arg1}")
print(f"second argument: {arg2}")


