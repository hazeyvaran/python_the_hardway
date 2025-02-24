"""
Adding flags like --verbose to enable detailed output

"""

import argparse

parser = argparse.ArgumentParser(description="Python script with a verbose flag")

parser.add_argument("name", type=str, help="Enter your name")
parser.add_argument("--verbose", action="store_true", help="enable verbose output")


args = parser.parse_args()

if args.verbose:
    print(f"verbose mode enabled")
print(f"hello, {args.name}")


