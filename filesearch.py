import pathlib


def search_files(dir:str, recursive:bool, rash:str ='*',name:str='*'):
    print(")___(")
    files = list()
    if(rash != '' and name != ''):
        if(recursive):
            print("recursive")
            recursive_find(dir,files,name,rash)
        else:
            print("no recursive")
            no_recursive_find(dir,name,rash,files)
    
    
def recursive_find(dir:str,massive:list,name:str='*', rash:str='*'):
    print("rec_find")
    searchable = name + '.' + rash
    path = pathlib.Path(dir)
    for child in path.rglob(searchable):
        print(child)

    
    
    
    
    
    

 

searching_directory = pathlib.Path()       
def search_dir(dirname_part: str, path: searching_directory, recursive: bool):
    directories = []
    if recursive:
        for directory in Path(path).rglob(f"{dirname_part}"):
            directories.append(directory) 
    elif not recursive:
        for directory in Path(path).glob(f"{dirname_part}"):
            directories.append(directory)



