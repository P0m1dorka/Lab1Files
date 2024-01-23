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
    print("End")
    
    
def no_recursive_find(dir:str,name:str='*', rash:str='*',massive:list=[]):
    searchable = name + '.' + rash
    path = pathlib.Path(dir)
    for child in path.glob(searchable):
        print(child)
    print("End")
    
    
    
    
    
    



