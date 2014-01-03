import time

#obtem tempo e armazena o valor na variavel v_str
gmt = time.gmtime(time.time())
fmt = '%H:%M:%S'
v_str = time.strftime(fmt, gmt)

#delay de 5 segundos
#time.sleep(5)

text_file = open("logFile.txt", "w")
text_file.write("inicio: " + v_str + "\n \n")

gmt = time.gmtime(time.time())
v_str = time.strftime(fmt, gmt)
text_file.write("fim: " + v_str + "\n \n")
text_file.close()

#ler arquivo de log e printa
f = open('logFile.txt',"r")
for i in range(3):
    print str(i) + ': ' + f.readline(),

f.close()