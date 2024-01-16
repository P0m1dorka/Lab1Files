import pathlib


def search_files(dir:str, name:str, inDirDir:bool = 0, rash:str = " ", name_rash:str= ""):
    print(")___(")
    path = pathlib.Path(dir)
    files = list()
    for child in path.glob(name+'.*'):
        print(child)
    print("Hello world")



