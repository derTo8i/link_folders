from os import path, system, remove
from tkinter.filedialog import askdirectory

def folder(title:str | None):
    path = askdirectory(title=title)
    while path == "":
        askdirectory(title=title)
    return path

def setup():
    folder_original = folder("Original")
    folder_link_parent_path = folder("Parentpath")
    foldername = input("Input foldername: ")

    folder_link = path.join(folder_link_parent_path, foldername)

    while foldername == "" or path.exists(folder_link):
        foldername = input("file exists or foldername is not a text. Please input new name: ")
        folder_link = path.join(folder_link_parent_path, foldername)

    print(folder_original)
    print(folder_link)

    system("sudo mklink /J " + '"' + folder_link + '" '+ '"' + folder_original + '" ')


if __name__ == "__main__":
    setup()

#system("Echo off")