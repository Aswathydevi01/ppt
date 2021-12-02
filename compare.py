import argparse
import re
import sys

from helpers import lines, sentences


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("__lines",action="store_true",help="comparelines")
    group.add_argument("__sentences",action="store_true",help="comparelines")
    parser.add_argument("FILE1",help="file to compare")
    parser.add_argument("FILE2", help="file to compare")
    args = vars(parser.parse_args())
    try:
        with open(args["FILE1"],"r") as file:
            file1 = file.read()
    except IOError:
        sys.exit(f"Could not read {args['FILE1']}")
    try:
        with open(args["FILE2"],"r") as file:
             file2 = file.read()
    except IOError:
        sys.exit(f"Could not read {args['FILE2']}")
    if args["lines"]:
        matches = lines(file1,file2)
    elif args["sentences"]:
        matches = sentences(file1,file2)

    for match in sorted(matches,key=len,reverse=True):
        print(match.replace("\n","\\n").replace("\r","\\r"))
def positive(string):
    value = int(string)
    if value <=0:
        raise argparse.ArgumentTypeError("invalid length")
    return value
if __name__ == "__main__":
    main()
