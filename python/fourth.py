def kmm(first, second):

    if first > second:
        greater = first
    else:
        greater = second

    while True:
        if ((greater % first == 0) and (greater % second == 0)):
            kmm = greater
            break
        greater += 1

    return kmm


first = input('Enter first number : ')
second = input('Enter second number : ')

print("kmm : ", kmm(int(first), int(second)))
