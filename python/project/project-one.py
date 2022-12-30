from colorama import Fore, Back, Style


def show_menu(items):
    while True:
        print(Fore.YELLOW + '\n Menu options :\n' + Style.RESET_ALL)

        # menu options :
        for index, item in enumerate(items):
            if(index == 0):
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
    print('perimeter : ' , perimeter)
    print('area : ' , area)


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

    print('\n\n ' + Fore.YELLOW + menuItems[0])
    print(' ' + '=' * len(menuItems[0]) + Fore.RESET + '\n')
    a = float(getInput(Fore.GREEN + ' #' + Fore.RESET + 'Enter the size of the side of the square: ','number'))

    printResult(a*a, a*4)


def rectangle():
    print('\n\n ' + Fore.YELLOW + menuItems[1])
    print(' ' + '=' * len(menuItems[1]) + Fore.RESET + '\n')
    a = float(getInput(Fore.GREEN + ' #' + Fore.RESET + 'Enter the length of the rectangle: ', 'number'))
    b = float(getInput(Fore.GREEN + ' #' + Fore.RESET + 'Enter the width of the rectangle: ', 'number'))

    printResult(a*b, (a*2) + (b*2))

    return 'rectangle'


def triangle():
    return 'triangle'


def circle():
    return 'circle'


def trapezoid():
    return 'trapezoid'


def cylinder():
    return 'cylinder'


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


# show menu to user and get number of menu item
selectedItem = show_menu(menuItems)

# fire actions that user selected
fire_menu_action(selectedItem)
