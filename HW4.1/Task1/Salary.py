from pathlib import Path


# open file and read them:
def total_salary(path):
    try:
        with open (path, "r", encoding= 'utf8') as file: 
        lines = [el.strip() for el in file.readlines()]

#total salary is now set at 0
        total = 0
        workers = 0


        for line in lines:
            name, salary_str = line.split(',') # -> list ["name", "salary"]
            salary  = int(salary_str)
            total += salary
            workers += 1

        if workers == 0:
            return (0,0)
            
        average_salary = total / workers
        return (total, average_salary)
    

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return {}




total, average = total_salary("workers.txt")      
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")