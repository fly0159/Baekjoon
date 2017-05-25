def poster(slice_list, max_size):
    wall = [ None ] * max_size

    for start, end, poster_owner in slice_list:
        wall[ start:end ] = str( poster_owner ) * (end - start)

    print( len( set( wall ) ) - 1 )


if __name__ == '__main__':
    slice_list = [ ]
    max_size = 0

    index = int( input() )

    for index in range( 1, index + 1 ):
        start, end = input().split()

        start = int( start )
        end = int( end )

        if end > max_size:
            max_size = end

        slice_list.append( (start, end + 1, index) )

    poster( slice_list, max_size )
