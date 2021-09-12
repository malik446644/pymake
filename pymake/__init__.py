import os
import os.path, time
import subprocess

def mkdir(new_directory_name):
    """making a new directory"""

    # getting the project folder full path 
    current_directory = os.getcwd()

    # getting the new directory full path
    path = os.path.join(current_directory, new_directory_name)

    # error handling if the folder doesnt exist
    try:
        os.mkdir(path)
    except:
        print("[WARNING] " + new_directory_name + " folder already exist")

def dcmd(source_file, dependant_file, cmd_arr):
    """executing shell command if the dependant file is older than the source file"""

    # getting the project folder full path 
    current_directory = os.getcwd()

    # getting the full path of the two files
    source_path = os.path.join(current_directory, source_file)
    dependant_path = os.path.join(current_directory, dependant_file)

    # executing commands if the dependant file does not exists
    if(os.path.isfile(dependant_path) != True):
        cmd(cmd_arr)
        return

    # getting the last time the two files were modified
    source_last_modified = os.path.getmtime(source_path)
    dependant_last_modified = os.path.getmtime(dependant_path)

    # executing command if the dependant file was older than the source file
    if(source_last_modified > dependant_last_modified):
        cmd(cmd_arr)
    else:
        print("[WARNING] " + source_file + " file did not change")

def cmd(cmd_arr):
    """executing shell command"""

    print(" ".join(cmd_arr))
    subprocess.run(cmd_arr, shell=True)

def rmdir(folder_path):
    """removes a directory"""

    current_directory = os.getcwd()

    if(os.path.isdir(folder_path) == False):
        print("[WARNING] the directory <" + folder_path + "> does not exist!")
        return

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(os.path.join(current_directory, folder_path))
    print("[info] successfully cleaned <" + folder_path + "> directory")

def rmindir(folder_path):
    """removing only the files and directories inside a directory"""

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    print("[info] successfully cleaned the files or folders inside <" + folder_path + "> directory")

def add_str_to_arr_elements(arr, before_str, after_str):
    """adding string before and after every string item in an array of strings"""
    arr2 = []
    for item in arr:
        arr2.append(before_str + item + after_str)
    return arr2

def get_names_by_type(path):
    src_names = []
    src_names_with_path = []
    for root, dirs, files in os.walk(path, topdown=False):
        if (root == path): root = ""
        for name in files:
            print(f'<{name}> lives in "{root}"')
            src_names.append(name)
            src_names_with_path.append(os.path.join(root, name))
    return (src_names, src_names_with_path)