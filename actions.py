from employee_management.add_employee import add_employee
from employee_management.change_employee import change_employee
from employee_management.delete_employee import delete_employee
from employee_management.search_employee import search_employee
from employee_management.displaying_employee import displaying_employee
from data_io import update_data


def actions(empls_list, saved_empls_list):
    
    while True:
        try:
            action = int(input("Choose action: 1-add employee data | 2-change employee data | 3-delete employee data | 4-search employee data | 5-displaying employee data: | 6-exit "))
            
            match action:
                case 1: add_employee(empls_list)
                case 2: change_employee(empls_list)
                case 3: delete_employee(empls_list)
                case 4: search_employee(empls_list, saved_empls_list)
                case 5: displaying_employee(empls_list, saved_empls_list)
                case 6: update_data(empls_list)
                case _: raise ValueError ("Invalid action selected.") # throw error if action not = 1,2,3,4,5 
        except ValueError:
            print("There are no such options")