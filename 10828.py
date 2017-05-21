stack = [ ]


def push(number):
    stack.append( number )


def pop():
    print( -1 if len( stack ) == 0 else stack.pop() )


def size():
    print( len( stack ) )


def empty():
    print( 1 if len( stack ) == 0 else 0 )


def top():
    print( -1 if len( stack ) == 0 else stack[ -1 ] )


if __name__ == '__main__':
    number = int( input() )

    for _ in range( number ):
        fn_arg = input()
        if fn_arg.startswith( 'push' ):
            fn, arg = fn_arg.split()
            eval( fn + "(" + arg + ")" )
        else:
            eval( fn_arg + "()" )
