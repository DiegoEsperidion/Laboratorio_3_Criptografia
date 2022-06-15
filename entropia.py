from hash import Iniciar,md5,sha1,sha256 #Importar las funciones de el archivo hash
from math import log #Para calcular el logaritmo de la entropia
pal= "123456"
p = Iniciar(pal)
md = md5(pal)
sh = sha1(pal)
sh2 = sha256(pal)
#Calcular la entropia de una palabra
def entropia(palabra):
    L = len(palabra)
    N = 94
    H = L*log(N,2)
    return H

print("Entropia de la palabra: ", entropia(p))
print("Entropia de la palabra md5: ", entropia(md))
print("Entropia de la palabra sha1: ", entropia(sh))
print("Entropia de la palabra sha256: ", entropia(sh2))

#CAlcular entropia de md5

