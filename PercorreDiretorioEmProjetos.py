import os


def leprojet(projetos):
    todoscommit=[]
    for projeto in os.listdir(projetos):
        pathprojeto = projetos + '/'+ projeto
        todoscommit.append( pathprojeto)
    
    #print('todoscommit', todoscommit)
    
    return todoscommit

#        for commit in os.listdir(pathprojeto):
 #           pathcommit= pathprojeto + '\\'+ commit
          #  print(pathcommit)    

#leprojet('C:\Analysis\MPSolve')