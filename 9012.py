def pair_check(string_input):
    queue_data = list(string_input)
    count = 0

    if queue_data[-1] == '(' or queue_data[0] == ')':
        return "NO"

    for data in queue_data:
        if count < 0:
            return "NO"
        if data == '(':
            count += 1
        else:
            count -= 1

    return "NO" if count != 0 else "YES"


if __name__ == '__main__':
    number = int(input())

    for _ in range(number):
        print(pair_check(input()))
