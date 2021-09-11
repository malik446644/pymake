import sys
import pymake as pm

# creating two important files
pm.mkdir("tmp")
pm.mkdir("bin")

# names of the source files
src_names = ["main"]

# compiling the source files
print(">>>>>>>>>>>>    COMPILING    <<<<<<<<<<<<")
pm.fcmd(
    "src/" + src_names[0] + ".c",
    "tmp/" + src_names[0] + ".o", 
    [
        "gcc", 
        "-c", 
        "-o", 
        "tmp/" + src_names[0] + ".o", 
        "src/" + src_names[0] + ".c"
    ]
)

# linking the object files
print(">>>>>>>>>>>>    LINKING    <<<<<<<<<<<<")
names_with_path = pm.add_str_to_arr_elements(src_names, "tmp/", ".o")
pm.cmd(
    [
        "gcc", 
        "-o", 
        "bin/main.exe", 
        " ".join(names_with_path)
    ]
)