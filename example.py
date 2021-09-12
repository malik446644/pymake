import sys
import pymake as pm

#---------------------------------------------------------------------------------------------#
# if no arguments were given only this part of the code will work when you execute this file. #
#---------------------------------------------------------------------------------------------#
if (len(sys.argv) == 1):
    # creating two important files
    print("\n>>>>>>>>>>>>    CREATING FOLDERS    <<<<<<<<<<<<")
    pm.mkdir("tmp")
    pm.mkdir("bin")

    # names of the source files
    src_names, src_names_with_path = pm.get_names_by_type("src", ".c")

    # compiling the source files
    print("\n>>>>>>>>>>>>    COMPILING    <<<<<<<<<<<<")
    for i in range(len(src_names)):
        pm.dcmd(
            f"{src_names_with_path[i]}.c",
            f"tmp/{src_names[i]}.o", 
            [
                "gcc", 
                "-c", 
                "-o", 
                f"tmp/{src_names[i]}.o", 
                f"{src_names_with_path[i]}.c"
            ]
        )

    # linking the object files
    print("\n>>>>>>>>>>>>    LINKING    <<<<<<<<<<<<")
    names_with_path = pm.add_str_to_arr_elements(src_names, "tmp/", ".o")
    pm.cmd(
        [
            "gcc",
            "-o",
            "bin/app.exe",
        ] + names_with_path
    )
    
#---------------------------------------------------------------------------------------------------------#
# if "clean" argument was given when executing this file then only this part of the code will be executed #
#---------------------------------------------------------------------------------------------------------#
elif ("clean" in sys.argv):
    print("\n>>>>>>>>>>>>    CLEANING    <<<<<<<<<<<<")
    pm.rmdir("bin")
    pm.rmdir("tmp")