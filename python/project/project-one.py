from colorama import Fore, Back, Style

menuItems = [
    'calculate Perimeter and area of square',
    'calculate Perimeter and area of rectangle',
    'calculate Perimeter and area of triangle',
    'calculate Perimeter and area of circle',
    'calculate Perimeter and area of trapezoid',
    'calculate Perimeter and area of cylinder',
]


def show_menu(items):
    while True:
        print(Fore.YELLOW + '\n Menu options :\n' + Style.RESET_ALL)

        # menu options :
        for index, item in enumerate(items):
            print(' \b ' + Fore.BLUE +
                  '[' + str(index+1) + '] : ' + Fore.RESET + item)
        # get user action number
        selectedItem = input(
            Fore.GREEN + '\n #Enter number of blow actions that you want to do : \b ' + Fore.YELLOW + Fore.RESET)

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


# def fire_menu_action():


# show menu to user and get number of menu item
selectedItem = show_menu(menuItems)
print(selectedItem)
# fire_menu_action(selectedItem)
