from hash import Iniciar,md5,sha1,sha256,sha1solo,sha256solo,md5solo#Importar las funciones de el archivo hash
from math import log #Para calcular el logaritmo de la entropia
pal= "abuelo"
p = Iniciar(pal)
md = md5solo(pal)
sh = sha1solo(pal)
sh2 = sha256solo(pal)
#Calcular la entropia de una palabra
def entropia(palabra):
    L = len(palabra)
    N = 94
    H = L*log(N,2)
    return H

def entropiahash(palabra):
    L = len(palabra)
    N = 36
    H = L*log(N,2)
    return H


print("Entropia de la palabra: ", entropia(p))
print("Entropia de la palabra md5: ", entropiahash(md))
print("Entropia de la palabra sha1: ", entropiahash(sh))
print("Entropia de la palabra sha256: ", entropiahash(sh2))

#CAlcular entropia de md5

