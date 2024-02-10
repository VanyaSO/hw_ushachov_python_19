from employee_management.get_employee_data import get_employee_surname
from employee_management.save_found_employee import save_found_employee
from data_io import save_data

def search_employee(empls_list, saved_empls_list):
    found_list = {}
    
    if len(empls_list) > 1:
        while True:
            surname = get_employee_surname().capitalize()
            
            if surname not in empls_list:
                print("Not found employee")
                break
        
            for empl in empls_list:
                name = empl
                age = empls_list[empl]["age"]
                position = empls_list[empl]["position"]
                
                if empl == surname:
                    print(f"Information about {surname}")
                    print(f"Age: {age}, Position: {position}")
                    found_list[name] = {"age": age, "position": position}        
                
                break
            
        if len(found_list) >= 1:
            if save_found_employee(found_list, saved_empls_list):                
                save_data(saved_empls_list)
    else:
        print("List empty")
        