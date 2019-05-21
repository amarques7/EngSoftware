import os
def listardiretorio(path,i):

    print ("path: ", path)
    print ("i: ",i)

    subdir = list()
    #r == root, d == directory, f == file
   
    for r, d, f in os.walk(path):
        for folder in d:
          subdir.append(os.path.join(r,folder))  
        
    print("subdir: ", subdir[i])
          
    return(subdir[i])        
  