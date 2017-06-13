def word_cheker(word):
    word_list = [ ]
    current_word = None
    for char in list( word ):
        if current_word is None:
            current_word = char
            word_list.append( current_word )

        if current_word != char:
            current_word = char
            word_list.append( char )
    return 1 if len( word_list ) == len( set( list( word ) ) ) else None


def group_word_checker(words):
    result = 0
    for word in words:
        if word_cheker( word ) == 1:
            result += 1
    return result


if __name__ == '__main__':
    words = [ ]
    scope = int( input() )
    for _ in range( scope ):
        words.append( input() )
    print(group_word_checker( words ))
