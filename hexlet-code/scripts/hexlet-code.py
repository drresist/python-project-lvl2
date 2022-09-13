import argparse

def main():
    """
    Enter point of application
    """
    parser = create_parser()
    args = parser.parse_args()
    print("Initial template")


def create_parser():
    """Create argument parser for input files."""
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    return parser

if __name__ == "__main__":
    main()


