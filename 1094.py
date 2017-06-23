def cal_stick(stick_length, stick = 64):
    sum = 0
    glue = 0
    save = 0
    save = stick_length

    while (sum != save):
        while (stick > stick_length):
            stick /= 2
        sum += stick
        stick_length -= stick
        glue += 1
        stick = 64
    print( glue )


if __name__ == '__main__':
    stick_length = int( input() )
    cal_stick( stick_length )
