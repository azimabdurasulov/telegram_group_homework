from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    ids = []
    for msg in data["messages"]:
        id = msg.get("from_id", False)
        if id and (id not in ids):
            ids.append(id)
    return ids