import argparse

# Creation of argument parser object
parser = argparse.ArgumentParser(description="list your favorite programing languages")

# Adding a required argument
parser.add_argument("name", type=str, help="Enter your name")

# Adding an optional argument
parser.add_argument("--languages", nargs="+", help="list your favorite programing languages.")

# Parses the arguments
args = parser.parse_args()

# Output results
print(f"{args.name}'s favorite programing languages are: {','.join(args.languages) if args.languages else 'not provided'}")


