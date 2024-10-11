from os import path, system
from tkinter.filedialog import askdirectory


def create_folder_junction() -> int:
    """
    This function creates a junction link (symbolic link) between two folders. 
    
    @return -1 (int): 
    @return -2 (int): 
    """
    original_folder_path = "D:/#/"#askdirectory(title="Original")
    if not original_folder_path: return -1
    parent_folder_path = "D:/" #askdirectory(title="Parentpath")
    if not parent_folder_path: return -2
    junction_folder_name = "a" #input("Input foldername of the new folder (symbolic link): ")


    print("Overview: ")
    print(f"Original {original_folder_path}")
    print(f"Parent {parent_folder_path}")
    print(f"Name {junction_folder_name}")
    
    new_folder_path = path.join(parent_folder_path, junction_folder_name)
    while junction_folder_name == "" or path.exists(new_folder_path):
        junction_folder_name = input(f"Folder {new_folder_path} or foldername is not a text. Please input new name: ")
        new_folder_path = path.join(parent_folder_path, junction_folder_name)

    print(original_folder_path)
    print(new_folder_path)
    
    command = ("sudo mklink /J " + '"' + new_folder_path.replace("/", "\\") + '" '+ '"' + original_folder_path.replace("/", "\\") + '"')
    print(f"-{command}-")
    system(command)

def main():
    result = create_folder_junction()
    match result: 
        case -1:
            exit
        case -2: 
            exit

if __name__ == "__main__":
    main()