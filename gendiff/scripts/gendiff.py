import argparse


def main() -> None:
    build_parser()
    print('hello world')


def build_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    return parser.parse_args()


if __name__ == '__main__':
    main()
