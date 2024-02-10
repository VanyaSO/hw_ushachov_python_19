from employee_management.get_employee_data import get_employee_surname
from employee_management.get_employee_data import get_employee_age
from employee_management.get_employee_data import get_employee_position

def change_employee(empls_list):
    if len(empls_list) > 1:
        while True:
            surname = get_employee_surname()
            if surname.capitalize() not in empls_list:
                print("Not found employee") 
            break

        for empl in empls_list:
            if empl.lower() == surname.lower():
                    
                while True:
                    change_data = input("What do you want to change? (age / position / exit) : ")

                    if change_data.lower() == "age":
                        empls_list[empl]["age"] = str(get_employee_age())
                    elif change_data.lower() == "position":
                        empls_list[empl]["position"] = get_employee_position()
                    elif change_data == "exit":
                        break
                    else:
                        print("Enter: age / posotion / exit ")
                        continue
                    break
            break
    else:
        print("List empty")