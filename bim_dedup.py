#!python3
import sys
import typing
import argparse

def main(in_file: typing.TextIO):
    rs_ids = dict()
    for line in in_file:
        elements = line.split()
        rs_id = elements[1]
        if rs_id in rs_ids:
            count = rs_ids[rs_id]
            rs_ids[rs_id] = count + 1
            elements[1] = rs_id + "_" + str(count)
        else:
            rs_ids[rs_id] = 1
        print("\t".join(elements))



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
        Deduplicate PLINK BIM files.
        This tool replaces duplicated rsIds in BIM files with unambiguous ones.
        Outputs the result to STDOUT.
        Will not check the input for compliance with the specification.
        However, the rsId is expected to be in the second column.
    """)
    parser.add_argument("input", type=str, nargs="?", default="-", help="The BIM file to read in. Defaults to STDIN if '-' or no value is passed")
    args = parser.parse_args()

    if args.input == "-":
        main(sys.stdin)
    else:
        with open(args.input, 'r') as in_file:
            main(in_file)
