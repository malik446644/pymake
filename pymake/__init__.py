import os
import os.path, time
import subprocess

def mkdir(new_directory_name):
    # getting the project folder full path 
    current_directory = os.getcwd()

    # getting the new directory full path
    path = os.path.join(current_directory, new_directory_name)

    # error handling if the folder doesnt exist
    try:
        os.mkdir(path)
    except:
        print("[INFO] " + new_directory_name + " folder already exist")

def fcmd(source_file, dependant_file, cmd_arr):
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
        print("[INFO] " + source_file + " file did not change")

def cmd(cmd_arr):
    print(" ".join(cmd_arr))
    subprocess.run(cmd_arr, shell=True)

def add_str_to_arr_elements(arr, before_str, after_str):
    arr2 = []
    for item in arr:
        arr2.append(before_str + item + after_str)
    return arr2