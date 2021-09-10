import os

def mkdir(new_directory_name):
    current_directory = os.getcwd()
    path = os.path.join(current_directory, new_directory_name)
    try:
        os.mkdir(path)
    except:
        print("[WARNING] " + new_directory_name + " does already exist")