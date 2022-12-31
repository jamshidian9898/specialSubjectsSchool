def get_point_position():
    while True:
        position = input('Enter point position and septate with comma ( sample : x,y ): ')
        position = position.split(',')
        if(len(position) == 2):
            return position
        print('input is not valid. enter like sample: x,y ')

def distance(first, second):
    a = int(first[0]) - int(second[0])
    b = int(first[1]) - int(second[1])
    return (((a * a) + (b * b)) ** (1/2))


first = get_point_position()
second = get_point_position()
distance = distance(first, second)

print('distance between [%s,%s] and [%s,%s] : %d'%(first[0],first[1],second[0],second[1],distance))