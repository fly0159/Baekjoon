def plastic_number(number):
    number_dict = {key: 0 for key in range( 10 )}
    for item in list( map( int, number ) ):
        number_dict[ item ] += 1
    number_dict[ 6 ] = number_dict[ 9 ] = (number_dict[ 6 ] + number_dict[ 9 ]) / 2 + (number_dict[ 6 ] + number_dict[
        9 ]) % 2
    max_key, max_value = max( number_dict.items(), key = lambda key: key[ 1 ] )

    print( int( max_value ) )


if __name__ == '__main__':
    number = input()
    plastic_number( number )
