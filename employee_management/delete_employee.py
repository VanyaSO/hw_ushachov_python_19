from employee_management.get_employee_data import get_employee_surname

def delete_employee(empls_list):
    if len(empls_list) > 1:
        while True:
            surname = get_employee_surname()
            if surname.capitalize() not in empls_list:
                print("Not found employee")
            break
            
        
        for empl in empls_list:
            if empl.lower() == surname.lower():
                del empls_list[empl]
                print(f"You delete {empl}")
                break
    else:
        print("List empty")