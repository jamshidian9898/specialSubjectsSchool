from colorama import Fore, Back, Style


def show_menu(items):
    while True:
        print(Fore.YELLOW + '\n Menu options :\n' + Style.RESET_ALL)

        # menu options :
        for index, item in enumerate(items):
            if (index == 0):
                continue
            print('    ' + Fore.BLUE +
                  '[' + Fore.RESET + str(index) + Fore.BLUE + ']' + Fore.RESET + ' : ' + item)

        print('    ' + Fore.BLUE +
              '[' + Fore.RESET + str(0) + Fore.BLUE + ']' + Fore.RESET + ' : ' + items[0])
        # get user action number
        selectedItem = input(
            Fore.GREEN + '\n #' + Fore.RESET + 'Enter number of upper actions that you want to do: \b ')

        # validate menu item
        if (validate_menu_item(menuItems, selectedItem)):
            return selectedItem

        print(Fore.RED + '\n You entered wrong number of menu\'s items! try again. \b ' + Fore.RESET)


def validate_menu_item(menuItems, selectedItem):
    if (not selectedItem.isnumeric()):
        return False

    try:
        menuItems[int(selectedItem)]
        return True
    except IndexError:
        return False


def fire_menu_action(selectedItem):
    match selectedItem:
        case '0':
            endProgram()
        case '1':
            square()
        case '2':
            rectangle()
        case '3':
            triangle()
        case '4':
            circle()
        case '5':
            trapezoid()
        case '6':
            cylinder()
        case '7':
            Polygon()
        case '8':
            cone()
        case '9':
            Sphere()
        case '10':
            oval()


def printResult(perimeter = None, area = None, volume = None):
    print('\n ' + Fore.YELLOW + '=' * 25 + Fore.RESET)

    if (perimeter is not None):
        print(Fore.YELLOW + ' |' + Fore.RESET +Fore.GREEN + '  perimeter : ' + Fore.RESET, perimeter)

    if (area is not None):
        print(Fore.YELLOW + ' |' + Fore.RESET +Fore.GREEN + '  area : ' + Fore.RESET, area)

    if (volume is not None):
        print(Fore.YELLOW + ' |' + Fore.RESET +Fore.GREEN + '  Volume : ' + Fore.RESET, volume)

    print(' ' + Fore.YELLOW + '=' * 25 + Fore.RESET + '\n')

def getInput(text, type):
    inp = input(text)
    while True:
        if (inp != ''):
            if ((type == 'number')):
                try:
                    return float(inp)
                except ValueError:
                    ':)'
                return inp
            elif ((type == 'string') and (not inp.isnumeric())):
                return inp

        inp = input(
            Fore.RED + ' Your entered value is not valid.Try Again : ' + Fore.RESET)


menuItems = [
    'Exit',
    'calculate Perimeter and area of square',
    'calculate Perimeter and area of rectangle',
    'calculate Perimeter and area of triangle',
    'calculate Perimeter and area of circle',
    'calculate Perimeter and area of trapezoid',
    'calculate Perimeter and area of cylinder',
    'calculate Perimeter and area of Polygon',
    'calculate Perimeter and area of Cone',
    'calculate Perimeter and area of Sphere',
    'calculate Perimeter and area of oval',
]


def square():

    print('\n\n ' + Fore.YELLOW + menuItems[1])
    print(' ' + '=' * len(menuItems[1]) + Fore.RESET + '\n')

    a = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
              'Enter the size of the side of the square: ', 'number'))

    printResult(a*a, a*4)


def rectangle():
    print('\n\n ' + Fore.YELLOW + menuItems[2])
    print(' ' + '=' * len(menuItems[2]) + Fore.RESET + '\n')

    a = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
              'Enter the length of the rectangle: ', 'number'))
    b = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
              'Enter the width of the rectangle: ', 'number'))

    printResult(a*b, (a*2) + (b*2))


def triangle():
    print('\n\n ' + Fore.YELLOW + menuItems[3])
    print(' ' + '=' * len(menuItems[3]) + Fore.RESET + '\n')

    base = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                          'Enter the size of the base of the triangle: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the size height of the triangle: ', 'number'))

    printResult((base * height) / 2, base * 3)


def circle():
    print('\n\n ' + Fore.YELLOW + menuItems[4])
    print(' ' + '=' * len(menuItems[4]) + Fore.RESET + '\n')

    diameter = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                              'Enter the diameter of the circle: ', 'number'))

    printResult((3.14 * (diameter/2) * (diameter/2)), 3.14 * diameter)


def trapezoid():
    print('\n\n ' + Fore.YELLOW + menuItems[5])
    print(' ' + '=' * len(menuItems[5]) + Fore.RESET + '\n')

    bigBase = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                             'Enter the big base of the trapezoid: ', 'number'))
    smallBase = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                               'Enter the small base of the trapezoid: ', 'number'))
    firstSide = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                               'Enter the one side of the trapezoid: ', 'number'))
    secondSide = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                                'Enter the other side of the trapezoid: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the trapezoid: ', 'number'))

    printResult(((bigBase + smallBase) / 2) * height,
                bigBase + smallBase + firstSide + secondSide)


def cylinder():
    print('\n\n ' + Fore.YELLOW + menuItems[6])
    print(' ' + '=' * len(menuItems[6]) + Fore.RESET + '\n')

    radius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the radius of the base surface of the cylinder: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the cylinder: ', 'number'))

    baseArea = (3.14 * (radius*radius))
    sideArea = (((2*3.14) * radius) * height)

    printResult((baseArea * 2) + sideArea, 2 * ((radius*2) + height))


def Polygon():
    print('\n\n ' + Fore.YELLOW + menuItems[7])
    print(' ' + '=' * len(menuItems[7]) + Fore.RESET + '\n')

    sidesCount = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                                'Enter the sides count of the Polygon: ', 'number'))
    lengthOfSide = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                                  'Enter the one side length of the Polygon: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the Polygon: ', 'number'))

    perimeter = sidesCount * lengthOfSide
    area = (perimeter * height) / 2

    printResult(perimeter, area)


def cone():
    print('\n\n ' + Fore.YELLOW + menuItems[8])
    print(' ' + '=' * len(menuItems[8]) + Fore.RESET + '\n')

    slopeLength = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                                 'Enter the slope length of the Cone: ', 'number'))
    radius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the slope length of base of the Polygon: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the Cone: ', 'number'))

    area = (slopeLength * radius * 3.14)
    Volume = ((radius * radius) * height * 3.14) / 3

    printResult( None , area, Volume)


def Sphere():
    print('\n\n ' + Fore.YELLOW + menuItems[9])
    print(' ' + '=' * len(menuItems[9]) + Fore.RESET + '\n')

    radius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the slope length of base of the Polygon: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the Cone: ', 'number'))

    area = (4 * 3.14 * radius * radius)
    Volume = (3.14 * radius * radius * radius) * (4 / 3)

    printResult( None , area, Volume)


def oval():
    print('\n\n ' + Fore.YELLOW + menuItems[10])
    print(' ' + '=' * len(menuItems[10]) + Fore.RESET + '\n')

    bigRadius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                               'Enter the biggest radius of the oval: ', 'number'))
    smallRadius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                                 'Enter the smaller radius of base of the oval: ', 'number'))

    area = (bigRadius * smallRadius * 3.14)
    perimeter = (2 * 3.14 * (bigRadius * smallRadius / 2))

    printResult(perimeter, area)


def endProgram():
    exit(Fore.GREEN + '\n\n Exited by your choice. Have good day :)\n')


def wantsRoContinue():
    print('\n\n ' + Fore.YELLOW + "Do you want to continue or exit the program ?")
    print('    ' + Fore.BLUE +
          '[' + Fore.RESET + str(1) + Fore.BLUE + ']' + Fore.RESET + ' : continue and get happy :) ')
    print('    ' + Fore.BLUE +
          '[' + Fore.RESET + str(0) + Fore.BLUE + ']' + Fore.RESET + ' : exit the program')

    selection = getInput(Fore.GREEN + '\n #' + Fore.RESET +
                         'Enter number of upper actions that you want to do: ', 'number')

    if (selection != 1):
        endProgram()


while True:
    # show menu to user and get number of menu item
    selectedItem = show_menu(menuItems)

    # fire actions that user selected
    fire_menu_action(selectedItem)

    # ask do you want use again or exit
    wantsRoContinue()
