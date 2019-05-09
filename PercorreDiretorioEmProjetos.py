import os


def leprojet(projetos):
    todoscommit=[]
    for projeto in os.listdir(projetos):
        pathprojeto = projetos + '/'+ projeto
        todoscommit.append( pathprojeto)
    return todoscommit

#        for commit in os.listdir(pathprojeto):
 #           pathcommit= pathprojeto + '\\'+ commit
          #  print(pathcommit)    

#leprojet('C:/Users/amarq/OneDrive/Desktop/testeArquivo')