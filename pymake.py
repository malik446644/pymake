import sys
import pymake as pm

if (len(sys.argv) == 1):
    # creating two important files
    print("\n>>>>>>>>>>>>    CREATING FOLDERS    <<<<<<<<<<<<")
    pm.mkdir("tmp")
    pm.mkdir("bin")

    # names of the source files
    src_names = ["main"]

    # compiling the source files
    print("\n>>>>>>>>>>>>    COMPILING    <<<<<<<<<<<<")
    pm.fcmd(
        f"src/{src_names[0]}.c",
        f"tmp/{src_names[0]}.o", 
        [
            "gcc", 
            "-c", 
            "-o", 
            f"tmp/{src_names[0]}.o", 
            f"src/{src_names[0]}.c"
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
            " ".join(names_with_path)
        ]
    )

elif ("clean" in sys.argv):
    print("\n>>>>>>>>>>>>    CLEANING    <<<<<<<<<<<<")
    pm.rmdir("bin")
    pm.rmdir("tmp")