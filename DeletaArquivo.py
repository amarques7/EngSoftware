import os

def delete(dir_arq):
        
        test = os.listdir(dir_arq)
        for item in test:
          if not item.endswith(".dot"):
                os.remove(os.path.join(dir_arq, item))



#delete('c:/Users/amarq/OneDrive/Desktop/documentacao/latex')