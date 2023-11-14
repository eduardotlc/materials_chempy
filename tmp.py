import argparse
import materials_chempy.utils as mcpyut
import materials_chempy.cli_utils as mcpycliut
import sys

def add_arguments():
    parser = argparse.ArgumentParser(description="Test functions", add_help=False)
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-t", "--test", nargs='+')
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    parser.add_argument("-M", "--mplcfg", action="store_true")
    return parser
def main():

    parser = add_arguments()
    args = parser.parse_args()
    output_path, input_path = mcpycliut.gen_args(args)
    if args.test:
        print('aaaa')
        print('bbbbb')
    return()

if __name__ == "__main__":
    parser = add_arguments()
    args.append = parser.parse_args(['--test', 'bbbb', 'ccccc'])
    main()
