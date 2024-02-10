def get_employee_info():
    surname = get_employee_surname()
    age = get_employee_age()
    position = get_employee_position()
 
    return (surname, age, position)
           
def get_employee_surname():
    # Посчитал не нужным try так как все равно идет проверка через if и больше ниче ен вызывает ошибки 
    while True:
        surname = input("Surname: ")
        
        if surname.isdigit() or len(surname.strip()) < 3:
            print("Surname entered incorrectly")
            continue
        break
            
    return surname

def get_employee_age():
    while True:
        try:
            age = int(input("Age: "))
            
            if age <= 0 or age >= 100:
                raise ValueError ("Error")
            break
        except ValueError:
            print("Age entered incorrectly")
    return age
    
def get_employee_position():
    while True:
        position = input("Position: ")
        if position.isdigit() or len(position.strip()) < 2:
            print("Position entered incorrectly")
            continue
        break
        
    return position
    