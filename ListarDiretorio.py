import os
def listardiretorio(path,i):

    #print (path)
    #print (i)
 
    subdir = list()
    #r == root, d == directory, f == file
   
    for r, d, f in os.walk(path):
        for folder in d:
          subdir.append(os.path.join(r,folder))  
    return(subdir[i])        
