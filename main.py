import sys
import csv

#sys.path.append("C:\Codigos\Engenharia_Software")

#import teste
from teste import teste
from Parser import parser   

def main():
    param = sys.argv[1:]

    commit = param[0]
    dir_projeto = param[1]
    dir_result = param[2]
    localpath = param[3]
    nome_projeto = param[4]
  #  print('------------------------MAIN----------------------------------------------------------')
   # print('commit: ', commit)
   # print('dir_projeto: ', dir_projeto)
   # print('dir_resultado: ', dir_result)
   # print('local_path: ', localpath)
   # print ('posicao_projeto: ', nome_projeto)
   # print('------------------PARSER----------------------------------------------------------------')
 
    parser(commit, dir_projeto, dir_result, localpath, nome_projeto)
#
#-----------------------------------------------------
if __name__ == '__main__':
    main()
    #teste()