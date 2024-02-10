from employee_management.get_employee_data import get_employee_info

def add_employee(empls_list):
    while True:
        print("Enter infotmation about new employee")
        
        surname, age, position = get_employee_info()
        
        empls_list[surname.capitalize()] = dict(age = age, position = position)
        
        add_yet = input("Do you want to add another employee ? (yes / no): ")
        
        if add_yet != "yes":
            break
            