import base58 # Se usa la libreria base58 para convertir el texto plano en base58
import binascii #libreria para convertir el XOR obtenido en binario en ASCII
import fileinput
#Ingresamos la palabra a codificar en base58


#Transformar a Base58
def b58(hash):
    a = base58.b58encode(hash.encode()).decode() 
    return a

#Rellenar la palabra con caracteres especificos de manera de cumplir el largo de caracteres solicitados

def rellenar(palabra,pos):
    #cEsta funcion rellena una palabra menor a 55 caracteres con los caracteres contenidos en salt, se termina al tener 55 caracteres.
    salt=["1","A","a","B","b","C","c"]
    if pos == len(salt):
        pos=0
    if len(palabra) <55:
        pal=palabra+salt[pos]
        pos=pos+1
        pal=rellenar(pal,pos)
        return pal
    else:
        return palabra

def reducir(palabra,PosF,PosI,aux):
    #reduce una palabra mayor a 55 digitos, para esto suma el valor unicode en digitos de la palabra en las posiciones PosF y PosI, 
    #las cuales comienzan en el final e inicio respectivamete, luego lo agrega al auxiliar.
    if len(aux)==55:
        return aux
    else:
        A=ord(palabra[PosF])
        B=ord(palabra[PosI])
        posI=PosI+1
        posF=PosF-1
        aux.append(chr(A+B))
        pal=reducir(palabra,posF,posI,aux)
        return pal 
    
 
#Transform a to binary

def toBinary(a):
    l,m =[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m
    
# Usar XOR
def ConvertXOR(arr):
    c = []
    key="1011101"
    print("llave: ", key)
    for i in range(len(arr)):
        a = str(arr[i])
        c.append(bin(xor(a,key)))
    print("Hash en XOR: ",c)
    return c

def xor(a,b):
    y = int(a,2)^int(b,2)
    print(format(y,"b"))
    return y

def ConvertToASCII(X):
    arr  = b''
    for i in range(len(X)):
        c=X[i][2:]
        c=int(c,2)
        bi= binascii.unhexlify('%x' % c)
        print(c)
        print(bi)
        arr = arr + bi
    return arr

def tamaño(tam,hash):
    if(tam<55):
        hash = rellenar(hash,0)
        return hash
    elif(tam>55):
        aux = []
        aux2 =" "
        red = reducir(hash,tam-1,0,aux)
        for v in red
            aux2 = aux2+v
        hash = aux2
   return hash

def Iniciar(0):
    print("Ingrese el hash a codificar: ")
    hash = input()
    tam = len(hash)
    hash = tamaño(tam,hash)
    a = b58(hash)
    print("Mensaje codificado: " + a)
    print("")
    print("Hash en binario: ")
    print(toBinary(a))
    print("")
    arr = toBinary(a)
    X = ConvertXOR(arr)
    print("")
    print(ConvertToASCII(X))
    return 0

Iniciar(0)





#a = X[0][2:]
#a = int(a ,2)
#print(bin(a))
#print(a)
#
#print(binascii.unhexlify('%x' % a))









#Implement XOR of two binary numbers


