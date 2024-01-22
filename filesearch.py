import pathlib


def search_files(dir:str, name:str, inDirDir:bool = 0, rash:str = " ", name_rash:str=""):
    print(")___(")
    path = pathlib.Path(dir)
    files = list()
    for child in path.glob(name+'.*'):
        print(child)
    print("Hello world") 

searching_directory = pathlib.Path()       
def search_dir(dirname_part: str, path: searching_directory, recursive: bool):
    directories = []
    if recursive:
        for directory in Path(path).rglob(f"{dirname_part}"):
            directories.append(directory) 
    elif not recursive:
        for directory in Path(path).glob(f"{dirname_part}"):
            directories.append(directory)



