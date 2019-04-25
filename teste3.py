import csv
# abrindo o arquivo para escrita
with open('eggs5.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                        quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam']) # escreve tres strings no cs

#with open('eggs2.csv','w', newline='') as csvfile:
 #   spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  #  for row in spamreader:
   #     print(', '.join(row))



s = "('main', ['usage', 'cpio_trailer'])"
#h = s.split(" ")
#print (h)

for h in s.split(" "):
    print (h) 


    print ("########################3")
ultimobyteconfirmado = 3
ultimobyteenviado = 4
ultimobayteescrito = 9

if ultimobyteconfirmado <= ultimobyteenviado:
    print("ultimoByteConfiramdo")
else:
    print("ultimoByteEnviado")

print("************************")

if  ultimobyteenviado <= ultimobayteescrito:
        print("ultimoByteEnviado")
else:
    print("ultimoByteEcrito")

buffer =int(ultimobyteconfirmado - ultimobayteescrito)
print("Buffer:", buffer)
