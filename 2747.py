a, b = 1, 0

for _ in range( int( input() ) + 1 ):
    a, b = b, a + b

print( a )
