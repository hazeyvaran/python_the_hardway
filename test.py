import argparse

# create the object
parser = argparse.ArgumentParser(description="descrption")

# create the required argument
parser.add_argument("name", type=str, help="what is my name", default="red")

# create argument with multiple possible inputs
parser.add_argument("how many titties you want?", nargs="+", help="help me i want titties")

# parse the arguments
args = parser.parse_args()

# output
print()
