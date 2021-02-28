import operator
from collections import Counter
import re

class Department:

    def __init__(self, manager_id, department_id, department_name):
        self.manager_id = manager_id
        self.department_id = department_id
        self.department_name = department_name

class Employees:

    def __init__(self, name, phone_number, emp_number, date_of_birth, position, manager_id, department_id):
        self.name = name
        self.phone = phone_number
        self.emp_number = emp_number
        self.date_of_birth = date_of_birth
        self.position = position
        self.manager_id = manager_id
        self.department_id = department_id

#function to print a Menu
def printMenu():
    print("\n\n");
    print("         **********************************************************************************    ");
    print(f"\033[91m                                           MENU                                    \033[0m");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |1. Read Data.                                                                   |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |2. Sort.                                                                        |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |3. Fetch entry depending on emp_number                                          |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |4. Count number of employees that are in the same departmentID                  |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |5. Print employee’s name and numbers given Position.                            |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |6.Print employee’s department details depending on emp_number                   |    ");
    print("         |--------------------------------------------------------------------------------|    ");
    print("         |7.Exit                                                                          |    ");

# function to read a data an save into a 2 lists

def read_data(department_list, employees_list):
    d_text = open("Department.txt", 'r')
    department_data = d_text.readlines()
    e_text = open("Employee.txt", 'r')
    employees_data = e_text.readlines()

    for line in department_data:
        l = line.strip().split('|')
        department_list.append(Department(l[0], l[1], l[2]))

    for line in employees_data:
        l = line.strip().split('|')
        employees_list.append(Employees(l[0], l[1], int(l[2]), l[3], l[4], l[5], l[6]))

    print(f"\033[91mRead data done successfully . \033[0m")

# function to sort a Employee first by name if it same sort by number

def sort_emp(employees_list):
    employees_list = sorted(employees_list, key=operator.attrgetter('name', 'emp_number'), reverse=False)
    result_file = open("result1.txt", "w")
    for employees in employees_list:
        result_file.write("{}    :    {}\n\n".format(employees.name, employees.emp_number))
    print(f"\033[91mSort data done successfully in File. \033[0m")

# function to get the information about employee by given ID

def search_by_id(employees_list):
    em_num = int(input("please enter employee number :- "))
    for employees in employees_list:
        if (re.search(str(employees.emp_number) ,str(em_num))):
            print(f"\033[91m--------------------------------------------------------------------\033[0m")
            print(
                " employees name :  {}\n phone number :  {} \n employees number [unique] :  {}\n date of birth :  {} \n position :  {} \n manager id :   {} \n department id :  {} ".format(
                    employees.name, employees.phone, employees.emp_number, employees.date_of_birth, employees.position,
                    employees.manager_id, employees.department_id))
            print(f"\033[91m--------------------------------------------------------------------\033[0m")


            break

# function to get the name and the ID for employee by given Position

def search_by_postion(employees_list):
    print("Please enter position you want to search for :")
    emp_position = input()
    print("Employees name\t\t Employees ID ")
    for employees in employees_list:
        if (operator.contains(employees.position,emp_position)): #check if substring in a string of employee
            print("{}\t\t\t\t\t{}".format(employees.name, employees.emp_number))

    print(f"\033[91m--------------------------------------------------------------------\033[0m")

# function to Count number of employees that are in the same departmentID

def count(employees_list):
    countE = str(Counter(getattr(employees, 'department_id') for employees in employees_list))
    # will print like Counter({'1': 4, '2': 3}) so replace it
    countE = countE.replace("Counter", '')
    countE = countE.replace("{", '')
    countE = countE.replace("}", '')
    countE = countE.replace("(", '')
    countE = countE.replace(")", '')
    countE = countE.replace(":", '              ')

    countE=countE.split(",")
    # print(countE) # ["'1'               4", " '2'               3"]
    print(f"\033[91m--------------------------------------------------------------------\033[0m")
    print("Department_id   Number_of_employee")
    for line in countE :
      print("  {} ".format(line))
    print(f"\033[91m--------------------------------------------------------------------\033[0m")

# function to print a department details depends on employee number
temp=''
def print_employee_department(employees_list, department_list):
    emp_num = input("enter emp number :- ")
    for employees in employees_list:
        if (re.search(str(employees.emp_number) ,str(emp_num))):
            temp = str(employees.department_id)
            break
    print(f"\033[91m--------------------------------------------------------------------\033[0m")
    print("department name\t\t\tdepartment id\t\t\tmanager id")
    for department in department_list:
        if (re.search(str(department.department_id), str(temp))):
            print("{}                         {}                          {}".format(department.department_name, department.department_id, department.manager_id))
            break
    print(f"\033[91m--------------------------------------------------------------------\033[0m")

#####################################################################################################################
#                                            The Main to print menu

Department_list = []
Employees_list = []

printMenu()
while 1:

    option = int(input("\nPlease Enter Your Choice:"))
    if option == 1:
        try:
         read_data(Department_list, Employees_list)
        except:
            print(f"\033[91m              Logic Error!!!.            \033[0m")
            continue
    elif option == 2:
        try:
         sort_emp(Employees_list)
        except:
            print(f"\033[91m              Logic Error!!!.            \033[0m")
            continue
    elif option == 3:
        try:
         search_by_id(Employees_list)
        except:
            print(f"\033[91m              Logic Error!!!.            \033[0m")
            continue
    elif option == 4:
        try:
         count(Employees_list)
        except:
         print(f"\033[91m              Logic Error!!!.            \033[0m")
         continue
    elif option == 5:
        try:
         search_by_postion(Employees_list)
        except:
         print(f"\033[91m              Logic Error!!!.            \033[0m")
         continue
    elif option==6:
        try:
            print_employee_department(Employees_list, Department_list)
        except:
            print(f"\033[91m              Logic Error!!!.            \033[0m")
            continue
    elif option==7:
        print(f"\033[91m                  Good bye :) !              \033[0m")
        exit(1)
    else:
        print(f"\033[91m              Incorrect Choice!!!.            \033[0m")


