def chess(chess_pieces):
    result = 0
    chess_map = [
        [ 1, 0, 1, 0, 1, 0, 1, 0, ],
        [ 0, 1, 0, 1, 0, 1, 0, 1, ],
        [ 1, 0, 1, 0, 1, 0, 1, 0, ],
        [ 0, 1, 0, 1, 0, 1, 0, 1, ],
        [ 1, 0, 1, 0, 1, 0, 1, 0, ],
        [ 0, 1, 0, 1, 0, 1, 0, 1, ],
        [ 1, 0, 1, 0, 1, 0, 1, 0, ],
        [ 0, 1, 0, 1, 0, 1, 0, 1, ],
    ]

    for index1 in range( 8 ):
        for index2 in range( 8 ):
            if chess_map[ index1 ][ index2 ] and chess_pieces[ index1 ][ index2 ] == 'F':
                result += 1

    return result


if __name__ == '__main__':
    chess_pieces = [ [ ] for _ in range( 8 ) ]

    for index in range( 8 ):
        chess_pieces[ index ] = list( input() )

    print( chess( chess_pieces ) )
