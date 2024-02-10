from employee_management.save_found_employee import save_found_employee
from data_io import save_data


def displaying_employee(empls_list, saved_empls_list):
    found_list = {}
    
    if len(empls_list) > 1:
        found_value = input("To search, enter age / first letter of name: ").strip()
        
        for empl in empls_list:
            name = empl
            age = empls_list[empl]["age"]
            position = empls_list[empl]["position"]
            
            if (found_value.isdigit() and empls_list[empl]["age"] == found_value) or (name[0].lower()== found_value[0].lower()):
                print(f"{empl}, {empls_list[empl]["age"]} years, {empls_list[empl]["position"]}")
                found_list[name] = {"age": age, "position": position}

        if len(found_list) >= 1:
            if save_found_employee(found_list, saved_empls_list):                
                save_data(saved_empls_list)
        else:
            print("Not found employees")
    else:
        print("List empty")