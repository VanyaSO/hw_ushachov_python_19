
def save_found_employee(found_list, saved_empls_list):
    save_data_action = input("Want to save to file ? (yes / no): ")

    if save_data_action == "yes":
        saved_empls_list.update(found_list)
        return saved_empls_list
    else:
        return False