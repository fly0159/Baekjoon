def escape(coordinate):
    x, y, w, h = coordinate
    return min( x, min( y, min( w - x, h - y ) ) )


if __name__ == '__main__':
    coordinate = tuple( map( int, input().split() ) )
    print( escape( coordinate ) )