import config

def load_data(list_empls):
    with open(config.PATH_EMPLS_DATA, "r") as file:
        content = file.read().splitlines()
        
        for line in content:
            name, age, pos = line.split(",")
            list_empls[name] = {"age": age.strip(), "position": pos.strip()}


def save_data(saved_empls_list):
    
    if len(config.path_founed_empls_data.strip()) == 0:
        path = input("Enter name for file (example: new_list.txt): ")
        config.path_founed_empls_data = path 
        
    with open(config.path_founed_empls_data, "w") as file:
        for empl in saved_empls_list:
            name = empl
            age = saved_empls_list[empl]["age"]
            position = saved_empls_list[empl]["position"]
            
            data_string = f"{name}, {age}, {position}\n"
            
            file.write(data_string)

         
def update_data(list_empls):
    with open(config.PATH_EMPLS_DATA, "w") as file:
        print("\n")
        for empl in list_empls:
            name = empl
            age = list_empls[empl]["age"]
            position = list_empls[empl]["position"]
            
            data_string = f"{name}, {age}, {position}\n"
            
            file.write(data_string)
    exit()