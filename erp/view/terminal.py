def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title + ':')
    index = 1
    for option in list_options:
        if option != list_options[0]:
            print('(' + str(index) + ') ' + option)
            index += 1
    index = 0
    option = list_options[0]
    print('(' + str(index) + ') ' + option)


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    return print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int:
        print('@'+str(label)+': @'+str(result))
    elif type(result) == float:
        temp_result = result.split('.')
        result = temp_result[0] + temp_result[1][:2]
        print('@'+str(label)+': @'+str(result))
    elif type(result) == list or type(result) == tuple:
        print('@'+str(label)+': \n' )
        for item in result:
            print ('@'+str(item)+';')
    elif type(result) == dict:
        print('@'+str(label)+': \n' )
        for key, value in result.items():
            print('@'+str(key) + ': @'+str(value))


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    print('/-----------------------------------------------------------------------------------\\')
    for item in table:

        while len(item[1]) <= 22:
            item[1] += ' '

        while len(item[2]) <= 27:
            item[2] += ' '

        while len(item[0]) <= 15:
            item[0] += ' '

        print('|   '+item[0]+'   |   '+item[1]+'|   '+item[2]+'   |')

    print('\\-----------------------------------------------------------------------------------/')


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """

    return input(label + ' > ')


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    str_inputs = []
    for label_item in labels:
        if label_item != "id":
            item = get_input(label_item)
            str_inputs.append(item)
        else:
            str_inputs.append("PLACEHOLDER")
    return str_inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    return print('ERROR:',message)
