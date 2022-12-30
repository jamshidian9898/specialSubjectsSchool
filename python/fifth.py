
def bmm(first, second):
    greater = bmm = 0
    if first > second:
        greater = first
    else:
        greater = second
    for i in range(1, greater + 1):
        if first % i == 0 and second % i == 0:
            bmm = i
        return bmm


first = input('Enter first number : ')
second = input('Enter second number : ')

print("bmm : ", bmm(int(first), int(second)))
