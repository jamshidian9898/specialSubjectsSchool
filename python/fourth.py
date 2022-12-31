def kmm(first, second):
    return (first * second) / bmm(first , second)


def bmm(first, second):
    if first > second:
        bmm = second
    else:
        bmm = first
    while bmm > 1:
        if first % bmm == 0 and second % bmm == 0:
            return bmm
        bmm-= 1
    return 1

first = input('Enter first number : ')
second = input('Enter second number : ')

print("kmm : ", kmm(int(first), int(second)))
