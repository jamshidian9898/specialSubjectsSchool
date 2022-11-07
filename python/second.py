name = "Mohammad"
family = "Jamshidian"
age = "23"

print(name + '\b' + family)
print(age + '2')

print('\n')
print(family.upper())
print(family.lower())
print('\n')
print('hello, my name is %s %s.'%(name ,family))
print('hello, my name is {0:s} {1:s}. i am {2} years old.'.format(name, family, age))
print('\n')

# define list
UserAges = [22,45,10,78,54,23,18]

print('%s %s is %d years old.'%(name, family, UserAges[5]))
print('\n')
print('user ages :')
print(UserAges)
print('\n')
print('user ages 2:')
UserAges2 = UserAges
print(UserAges2)
print('\n')
print('user ages (from first to 5 index):')
print(UserAges[:6])
print('\n')
print('user ages -> (from 2 to 5 index):')
print(UserAges[2:6])
print('\n')
print('user ages -> (from 2 to end index):')
print(UserAges[2:])
print('\n')
print('user ages -> (all of the list with step 2):')
print(UserAges[::2])
print('\n')
print('user ages without %s %s\'s age:'%(name, family))
del UserAges[5]
print(UserAges)
print('\n')
print('add %s %s\'s age to user ages list:'%(name, family))
UserAges.append(23)
print(UserAges)
print('\n')
print('created by me :)')