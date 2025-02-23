import sys
#
# print("script name:", sys.argv[0])
# print("argument:", sys.argv[1:])


####################################

#accessing individual arguments
# if len(sys.argv) < 3:
#     print("usage: python script <arg1> <arg2>")
#     sys.exit(1)
#
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
#
# print(f"first argument: {arg1}")
# print(f"second argument: {arg2}")
#

######################
#
# #handling numeric arguments.
# # sys.argv stores arguments as strings, convert them when needed.
# # in the script shown below you can see that the args are converted to integers then added
# # this arg[arse thing seems to just create a list of items. the items are called out with the function
#
# if len(sys.argv) < 3:
#     print("You need to provide the appropriate number of arguments. <num3> <num2>")
#     sys.exit(1)
#
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# print(f"Sum: {num1 + num2}")

##############################################

# Checking the number of arguments

if len(sys.argv) <3:
    print("NO arguments have been privided!!!")
else:
    print(f"received {len(sys.argv) - 1} arguments: {sys.argv[1:]}")