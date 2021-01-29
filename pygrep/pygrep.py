import re
import argparse
import sys

def search(regex, fileInput):
    pattern = re.compile(regex)
    for line in fileInput.readlines():
        for match in pattern.findall(line):
            print(match, end=' ')
        print('')

def main():
    parser = argparse.ArgumentParser(description='A simple grep like program')
    parser.add_argument('-s', '--stdin', action='store_true', help='Accept input from stdin instead of a file')
    parser.add_argument('-f', '--file', type=str, help='Accpet input from a file')
    parser.add_argument('-r', '--regex', type=str, help='The pattern to serach for')
    
    args = parser.parse_args()

    if args.regex:
        if args.stdin:
            search(args.regex, sys.stdin)
        elif args.file:
            _file = open(args.file, 'r')
            search(args.regex, _file)
        else:
            print('Need either a file or stdin flag see the command help text')
    else:
        print('Need a pattern')

if __name__ == "__main__":
    main()
