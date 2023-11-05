import argparse
from .utils import client_help


def main():
    """

    Materials chempy package main fucntion, parsing specific submodule
    functions by user parsed flags.

    Returns
    -------
    None.

    """
    parser = argparse.ArgumentParser(description="Materials chempy package\
                                     main fucntion, parsing specific submodule\
                                     functions by user parsed flags.",
                                     add_help=False)

    # Add flags
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-m", "--msplot", action="store_true", help="Plot\
                        .mzML file in matplotlib.")
    parser.add_argument("-i", "--input", help="Input file path.", type=str)
    parser.add_argument("--resolution", type=float)
    parser.add_argument("-N", type=int)
    parser.add_argument("-n", type=int)
    parser.add_argument("-S", "--subtitle", type=str)
    parser.add_argument("--manual-peak", type=str)
    parser.add_argument("--manual-mz", type=list)
    parser.add_argument("--manual-label", type=list)
    args = parser.parse_args()
    if args.help:
        client_help()
    if args.msplot:
        print(f"{args.N}")
        # ms.msplot()
    return ()


if __name__ == "__main__":
    main()
