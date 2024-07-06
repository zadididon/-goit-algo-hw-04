from pathlib import Path
cats_list = []


def get_cats_info(path):

    try:
        with open (path, "r", encoding= 'utf8') as file: 
           lines = [el.strip() for el in file.readlines()]

        for line in lines:
            data = line.split(",") 

            cat_dict = {"id": data[0],
                        "name": data[1],
                        "age": data[2]
            }
            
            cats_list.append(cat_dict)
        
        return cats_list
    
    except FileNotFoundError:
     print(f"Error: File '{path}' not found.")
     return []

info_pro_kotikov = get_cats_info("pets_list.txt")
print(info_pro_kotikov)