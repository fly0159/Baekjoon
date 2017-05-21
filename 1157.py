def most_frequent_char(word):
    char_list = list( set( word ) )
    char_items_list = sorted( {char: word.count( char ) for char in char_list}.items(), key = lambda key: key[ 1 ],
                              reverse = True )

    if char_items_list[ 0 ][ 1 ] == char_items_list[ 1 ][ 1 ]:
        print( "?" )
    else:
        print( char_items_list[ 0 ][ 0 ] )


if __name__ == '__main__':
    word = input().upper()
    most_frequent_char( word )