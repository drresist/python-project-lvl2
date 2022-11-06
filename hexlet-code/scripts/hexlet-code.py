import argparse


def main():
    """
    Enter point of application
    """
    parser = create_parser()
    print("Initial template")


def create_parser()->argparse.ArgumentParser:
    """Create argument parser for input files."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", metavar="first_file", type=str)
    parser.add_argument("second_file", metavar="second_file", type=str)
    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        type=str,
        required=False,
        help="set format of output",
    )
    return parser


if __name__ == "__main__":
    main()
