import re


def croatia(string):
    return len( re.sub( '(c=|c-|dz=|lj|nj|s=|z=|d-)', '1', string ) )


if __name__ == '__main__':
    string = input()
    print( croatia( string ) )
