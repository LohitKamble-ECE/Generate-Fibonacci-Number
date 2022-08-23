import argparse


def parse():
    """Define, parse and return the command line argument."""
    args = argparse.ArgumentParser(description="Returns the nth fibonacci number.")
    args.add_argument(
        "-n",
        "--number",
        metavar="<n>",
        default=1,
        type=int,
        help="return the nth fibonacci number",
    )
    return args.parse_args()
