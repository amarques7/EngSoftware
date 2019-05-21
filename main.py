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
    posicao_projeto = param[4]
    print('------------------------MAIN----------------------------------------------------------')
    print('commit: ', commit)
    print('dir_projeto: ', dir_projeto)
    print('dir_resultado: ', localpath)
    print ('posicao_projeto: ', posicao_projeto)
    print('------------------PARSER----------------------------------------------------------------')
    parser(commit, dir_projeto, dir_result, localpath, posicao_projeto)
#    with open("c.csv", 'w', newline='') as csvfile:
#            spamwriter = csv.writer(csvfile, delimiter=';')
#            spamwriter.writerow(['TESTE']) # escreve st
  
 
#-----------------------------------------------------
if __name__ == '__main__':
    main()
    #teste()