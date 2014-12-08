import re

lista1 = open("RF00059_vs_UTR_Todas_sp_unicas","r")
listatxt = open("UTR_Todas_sp_unicas_linea.txt","r")
fulltxt = open("results.txt", 'w')
buscador = []
suma = re.compile('\d{2}[.]\d{1}')
orden = re.compile("[a-zA-Z]{3}[-][a-zA-Z]{1}[^ ]*")
x = []
counter = 0

for line in lista1:
    stq = re.findall(suma, line)
    data = re.findall(orden, line)
    if len(stq) > 0:
        if float(stq[0]) >= 35.8:
            if len(data) > 0:
                x.append(data[0])

byeduplicates = list(set(x))


for item in findhere:
    buscador.append(item)

for item in byeduplicates:
    cond = False
    for line in buscador:
        if cond:
            counter += 1
            print(str((counter/len(byeduplicates))*100)[0:5]+"% Done")
            fulltxt.write(item + "," + line)
            cond = False
            break
        if item in line:
            cond = True
lista1.close()
fulltxt.close()
