# Creation of argument parser object
# Adding a required argument
# Adding an optional argument
# Parses the arguments
# Output results


import argparse

parser = argparse.ArgumentParser(description="not sure what this descirption is for or how its used")
parser.add_argument("name", type=str, help="enter the name bro")
parser.add_argument("--ages", type=int, nargs="+", help="whatup homie cunt master 33")

arg = parser.parse_args()
print(f"what up {arg.name}, you such balls bro")
if arg.ages:
    print(f"your ages are {arg.ages}")
else:
    print("ugly you forgot to enter ages")





