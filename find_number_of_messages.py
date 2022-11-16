from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    sum = len(data["messages"])
    return sum
file_path = "data/result.json"
daa = read_data(file_path)
print(find_number_of_messages(daa)) 