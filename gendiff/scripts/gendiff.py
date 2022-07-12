import argparse


def main() -> None:
    buildParser()
    print('hello world')


def buildParser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    return parser.parse_args()


if __name__ == '__main__':
    main()
