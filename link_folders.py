from os import path, system, remove
from tkinter.filedialog import askdirectory


def get_dir_path(title:str | None):
    """
    Prompts the user to select a directory.
    
    @param title (str): The title of the directory selection dialog. Default is "Select a directory".
    @return path (str): The path of the selected directory.
    """
    path = askdirectory(title=title)
    while not path: 
        askdirectory(title=title)
    return path

def create_folder_junction():
    """
    This function creates a junction link (symbolic link) between two folders. 
    """
    original_folder_path = get_dir_path("Original")
    parent_folder_path = get_dir_path("Parentpath")
    junction_folder_name = input("Input foldername of the new folder (symbolic link): ")

    new_folder_path = path.join(parent_folder_path, junction_folder_name)

    while junction_folder_name == "" or path.exists(new_folder_path):
        junction_folder_name = input("file exists or foldername is not a text. Please input new name: ")
        new_folder_path = path.join(parent_folder_path, junction_folder_name)

    print(original_folder_path)
    print(new_folder_path)

    system("sudo mklink /J " + '"' + new_folder_path + '" '+ '"' + original_folder_path + '" ')


if __name__ == "__main__":
    create_folder_junction()

#system("Echo off")