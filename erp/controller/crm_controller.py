from model.crm import crm
from view import terminal as view


def list_customers():
    customer_table = crm.data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(customer_table)


def add_customer():
    customer_table = crm.data_manager.read_table_from_file(crm.DATAFILE)
    add_input_labels =  crm.HEADERS
    view.print_table(customer_table)
    all_inputs = view.get_inputs(add_input_labels)
    for item in all_inputs:
        if item == "PLACEHOLDER":
            item = crm.util.generate_id()
            all_inputs[0] = crm.util.generate_id()
    customer_table.append(all_inputs)
    crm.data_manager.write_table_to_file(crm.DATAFILE,customer_table)
    return add_input_labels


def update_customer():
    customer_table = crm.data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(customer_table)
    selected_customer = input("choose a customer by ID: ")
    for line in customer_table:
        if selected_customer in line[0]:
            selected_line = line
    selected_data = input("choose data what would like to modify (id/name/email/subscribed): ")
            
    if selected_data == "id":
        replaced_id = input("please enter a new id: ")
        selected_line[0] = replaced_id
    elif selected_data == "name":
        replaced_name = input("please enter a new name: ")
        selected_line[1] = replaced_name
    elif selected_data == "email":
        replaced_email = input("please enter a new email: ")
        selected_line[2] = replaced_email
    elif selected_data == "subscribed":
        replaced_sub = input("please enter a new subscribed: ")
        selected_line[3] = replaced_sub
    else:  
        print("invalid input!")

    crm.data_manager.write_table_to_file(crm.DATAFILE, customer_table, separator=';')



def delete_customer():
    customer_table = crm.data_manager.read_table_from_file(crm.DATAFILE)
    view.print_table(customer_table)
    which_id_input = view.get_input('Enter the user`s ID that you wish to delete: ')
    count = 0
    for item in customer_table: 
        if which_id_input in item[0]:
            del customer_table[count]
        count += 1
    crm.data_manager.write_table_to_file(crm.DATAFILE,customer_table)
    view.print_table(customer_table)


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
