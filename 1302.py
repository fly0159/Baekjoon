def bestseller(sold_book_list, sold_book_dict = {}, max_list = [ ]):
    for book in list( set( sold_book_list ) ):
        sold_book_dict[ book ] = sold_book_list.count( book )

    max_value = max( sold_book_dict.values() )

    for book, book_count in sold_book_dict.items():
        if book_count == max_value:
            max_list.append( book )

    print( sorted( max_list )[ 0 ] )


if __name__ == '__main__':
    scope = int( input() )
    sold_book_list = [ ]

    if isinstance( scope, int ):
        for _ in range( scope ):
            sold_book_list.append( input() )
        bestseller( sold_book_list )
