from colorama import Fore, Back, Style
import turtle


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
    return itemsFunctions.get(int(selectedItem), default)()


def printResult(perimeter, area):
    print('perimeter : ', perimeter)
    print('area : ', area)


def getInput(text, type):
    inp = input(text)
    while True:
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
    print('\n\n ' + Fore.YELLOW + menuItems[5])
    print(' ' + '=' * len(menuItems[5]) + Fore.RESET + '\n')

    radius = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the radius of the base surface of the cylinder: ', 'number'))
    height = float(getInput(Fore.GREEN + ' #' + Fore.RESET +
                            'Enter the height of the cylinder: ', 'number'))

    baseArea = (3.14 * (radius*radius))
    sideArea = (((2*3.14) * radius) * height)

    printResult((baseArea * 2) + sideArea, 2 * ((radius*2) + height))


def default():
    show_menu(items)


def endProgram():
    exit(Fore.GREEN + '\n\n Exited by your choice. Have good day :)\n')


itemsFunctions = {
    0: endProgram,
    1: square,
    2: rectangle,
    3: triangle,
    4: circle,
    5: trapezoid,
    6: cylinder,
}

while True:
    # show menu to user and get number of menu item
    selectedItem = show_menu(menuItems)

    # fire actions that user selected
    fire_menu_action(selectedItem)
