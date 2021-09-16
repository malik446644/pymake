import sys
import pymake as pm

#----------------#
# configurations #
#----------------#
compiler = "g++"
source_folder_name = "src"
source_files_extension = ".cpp"

#--------------------------------------------------------------------------------------------#
# if no arguments were given only this part of the code will work when you execute this file #
#--------------------------------------------------------------------------------------------#
if (len(sys.argv) == 1):
    # creating two important files
    print("\n>>>>>>>>>>>>    CREATING FOLDERS    <<<<<<<<<<<<")
    pm.mkdir("tmp")
    pm.mkdir("dist")

	# compiling shaders
    # print("\n>>>>>>>>>>>>    COMPILING SHADERS    <<<<<<<<<<<<")
    # pm.cmd(["D:/VulkanSDK/1.2.176.1/Bin32/glslc.exe", "./shaders/shader.vert", "-o", "./shaders/vert.spv"])
    # pm.cmd(["D:/VulkanSDK/1.2.176.1/Bin32/glslc.exe", "./shaders/shader.frag", "-o", "./shaders/frag.spv"])

    # names of the source files
    src_names, src_names_with_path = pm.get_names_by_type(source_folder_name, source_files_extension)

    # compiling the source files
    print("\n>>>>>>>>>>>>    COMPILING    <<<<<<<<<<<<")
    for i in range(len(src_names)):
        pm.dcmd(
            f"{src_names_with_path[i]}{source_file_extension}",
            f"tmp/{src_names[i]}.o", 
            [
                compiler, 
                "-c", 
                "-o", 
                f"tmp/{src_names[i]}.o", 
                f"{src_names_with_path[i]}{source_file_extension}",
                "-I./libraries/GLFW/include",
                "-ID:/VulkanSDK/1.2.176.1/Include",
                "-I./libraries/GLM",
                "-I./libraries/stbImage",
            ]
        )

    # linking the object files
    print("\n>>>>>>>>>>>>    LINKING    <<<<<<<<<<<<")
    names_with_path = pm.add_str_to_arr_elements(src_names, "tmp/", ".o")
    pm.cmd(
        [
            compiler,
            "-o",
            "app.exe",
        ] + names_with_path +
        [
            "-L./libraries/GLFW/lib",
            "-LD:/VulkanSDK/1.2.176.1/lib",
            "-lglfw3",
            "-lvulkan-1",
            "-lpthread",
            "-lgdi32",
        ]
    )
    
#---------------------------------------------------------------------------------------------------------#
# if "clean" argument was given when executing this file then only this part of the code will be executed #
#---------------------------------------------------------------------------------------------------------#
elif ("clean" in sys.argv):
    print("\n>>>>>>>>>>>>    CLEANING    <<<<<<<<<<<<")
    pm.rmdir("tmp")
    pm.rmdir("dist")