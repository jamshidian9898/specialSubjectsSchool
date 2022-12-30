# print stars in triangle shape
linesCount = 4
for i in range(1, linesCount+1):
    stars = ''
    for j in range(1, i+1):
        stars += '*'
    print(stars)
