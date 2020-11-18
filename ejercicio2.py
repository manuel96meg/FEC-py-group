import textwrap

class NuevaSecuencia:
    #un objeto nuevo por cada secuencia Nueva que se encuentra
    def __init__(self,secuenciaNueva=''):
        self.secuenciaNueva = secuenciaNueva

    def add(self,nuevo):
        self.secuenciaNueva += nuevo

    def mostrar(self):
        print('Esta secuencia : ',self.secuenciaNueva)

def mostrarLista(ListaSec):
    if ListaSec:
        for l in range(len(ListaSec)):
            ListaSec[l].mostrar()

def sacarDeLista(lista,n1,n2):
    #saca de la lista los elementos que ya se vieron con los indices "i" y "k"
    del lista[n1:n2+1]


#secRegex = re.compile(r'^AUG A|U|C|G* UUA|UGA|UAG')
secuencia = str(input('Ingrese una secuencia de ARN: '))
ListaSec= []
cant = 0 #cantidad de secuencias
secL = textwrap.wrap(secuencia,3) #dividir de a grupos de 3 la secuencia
#print(secL)

i = 0
while i < len(secL):
    if secL[i] == 'AUG':
    #pregunta si coincide con el inicio de la secuencia
        ObjSec = NuevaSecuencia()
        ObjSec.add(secL[i])
        k = 0
        while k < len(secL):
            ObjSec.add(secL[k])
            if ((secL[k] == 'UGA') or (secL[k] == 'UUA') or (secL[k] == 'UAG')):
            #pregunta si coincide con un final posible de la secuencia
                ListaSec.append(ObjSec)
                sacarDeLista(secL,i,k)
            k += 1
        continue
    i += 1

mostrarLista(ListaSec)
cant = len(ListaSec)
if cant == 0:
    print('No se han encontrado secuencias de ARN')
else:
    print(f'Se han encontrado {cant} secuencias de ARN')
