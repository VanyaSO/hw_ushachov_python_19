from actions import actions
from data_io import load_data

employees_list = {}
saved_list = {}


def main(empls_list, saved_empls_list):
    load_data(empls_list)
    actions(empls_list, saved_empls_list)
    
            
main(employees_list, saved_list)