from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    return [data["name"]]

file_path = "data/result.json"
daa = read_data(file_path)
print(find_all_users_name(daa))
