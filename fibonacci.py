from command_parser import parse
from gen_fib import nth_fib


def main():
    """Starting point of the progam."""
    args = parse()
    print(nth_fib(args.number))


if __name__ == "__main__":
    main()
