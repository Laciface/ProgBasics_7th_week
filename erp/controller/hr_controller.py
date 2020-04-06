from model.hr import hr
from view import terminal as view
import datetime

current_date = datetime.date.today()

def list_employees():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_table)


def add_employee():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    add_input_labels =  hr.HEADERS
    view.print_table(hr_table)
    all_inputs = view.get_inputs(add_input_labels)
    for item in all_inputs:
        if item == "PLACEHOLDER":
            item = hr.util.generate_id()
            all_inputs[0] = hr.util.generate_id()
    hr_table.append(all_inputs)
    hr.data_manager.write_table_to_file(hr.DATAFILE,hr_table)
    return add_input_labels


def update_employee():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_table)
    selected_customer = input("Choose a customer by ID")
    for line in hr_table:
        if selected_customer in line[0]:
            selected_line = line
    selected_data = input("choose data what would like to modify (id/name/birthday/department/clearance): ")

    if selected_data == "id":
        replaced_id = input("please enter a new id: ")
        selected_line[0] = replaced_id
    elif selected_data == "name":
        replaced_name = input("please enter a new name: ")
        selected_line[1] = replaced_name
    elif selected_data == "birthday":
        replaced_birthday = input("please enter a new birthday: ")
        selected_line[2] = replaced_birthday
    elif selected_data == "department":
        replaced_department = input("please enter a new clearance level: ")
        selected_line[3] = replaced_department
    elif selected_data == "clearance":
        replaced_clearance = input("please enter a new clearance level: ")
        selected_line[4] = replaced_clearance
    else:
        print("invalid input!")

    hr.data_manager.write_table_to_file(hr.DATAFILE, hr_table, separator=';')


def delete_employee():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_table)
    which_id_input = view.get_input('Enter the user`s ID that you wish to delete: ')
    count = 0
    for item in hr_table: 
        if which_id_input in item[0]:
            del hr_table[count]
        count += 1
    hr.data_manager.write_table_to_file(hr.DATAFILE,hr_table)
    view.print_table(hr_table)


def get_oldest_and_youngest():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    name_date ={}
    birth_dates = []
    for row in hr_table:
        pure_date = row[2].strip()
        birth_dates.append(pure_date)
        name_date[pure_date] = row[1].strip()
    print("\nThe oldest employee is: " + "\n" + str(name_date[sorted(name_date.keys())[0]]))
    print("\nThe youngest employee is:" + "\n" + str(name_date[sorted(name_date.keys())[-1]]))

def get_average_age():
    hr_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(hr_table)
    birth_dates = []
    ages = []
    for row in hr_table:    
        pure_date = row[2].strip()
        birth_dates.append(pure_date)
    for birthday in birth_dates:
        ages.append((current_date - datetime.datetime.strptime(birthday, '%Y-%m-%d').date()).days//365)
    print("\nThe average age is : " + str(int(sum(ages)/len(ages))) + '\n')
    

def next_birthdays():
    customer_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(customer_table)
    today = datetime.date.today()
    print(today)
    for item in customer_table:
        if item[2].strip()[-5:-1] == today[-5:-1]:
            print(item[0].strip()+" "+item[1].strip())


def count_employees_with_clearance():
    customer_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(customer_table)
    which_clearance = input("Enter the user's clearance level:")
    count = 0
    for item in customer_table:
        if item[4] >= which_clearance:
            count += 1
    print(count)


def count_employees_per_department():
    customer_table = hr.data_manager.read_table_from_file(hr.DATAFILE)
    view.print_table(customer_table)
    departments = dict()
    for item in customer_table:
        if item[3].strip() in departments:
            departments[item[3].strip()] += 1
        else:
            departments[item[3].strip()] = 1
    print(departments)


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
