import filesearch
if __name__ == '__main__':
    """
  # без рекурсии, знаем только название
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',0,name='f1')
    print("________________")
  # без рекурсии, знаем только расширение  
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',0,rash='txt')
    print("________________")
  # без рекурсии, знаем всё
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',0,rash='txt',name='f1')
    print("________________")
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',1,rash='txt',name='f1') 
    print("________________")
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',1,rash='txt') 
    print("________________")
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',1,name='f*') 
    print("hello world")
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',1) 
    filesearch.search_files('/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',0) 
     """
    filesearch.search_dir('*','/home/SherseLyaFam/ProgProjects/Python/Lab1/test_dir',True)