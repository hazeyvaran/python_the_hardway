import argparse

# create an argumentParser object
parser = argparse.ArgumentParser(description="Example script with argument")

# Add a positional argument (required)
parser.add_argument("name", type=str, help="Your name")

# Adds an optional argument with a default value
parser.add_argument("--age", type=int, help="enter your age", default=None)

# Parse the arguments
args = parser.parse_args()

# Output the results
print(f"\nHello, {args.name}!")
if args.age:
    print(f"\nyou are {args.age} years old\n")
else:
    print("\nAge was not provided!!!")