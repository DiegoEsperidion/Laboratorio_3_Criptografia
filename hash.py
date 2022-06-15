import base58 # Se usa la libreria base58 para convertir el texto plano en base58
import binascii #libreria para convertir el XOR obtenido en binario en ASCII
import hashlib #Libreria para encriptar con md5
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
    
 
#Transformar de Base58 a Binario

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
    print("Aplicando XOR a los binarios obtenidos con la llave:  ",c)
    return c

def xor(a,b):
    y = int(a,2)^int(b,2)
    format(y,"b")
    return y

#Iterar el valor de c para satisfacer el requerimiento de la funcion unhexlify
def iterar(c):
    while(c<32):
        c=c+c/2
    
    while(c>126):
        c=c-c/2
    return int(c)

#Transforma los bytes en un string
def toString(arr):
    return ''.join(map(chr, arr))

#Transforma el binario de XOR a ASCII
def ConvertToASCII(X):
    arr  = b""
    for i in range(len(X)):
        c=X[i][2:]
        c=int(c,2)
        c=iterar(c)
        bi= binascii.unhexlify('%x' % c)
        arr = arr + bi
    return toString(arr)
#Ajusta el tamaño del hash a 55 caracteres como minimo
def tamaño(tam,hash):
    if(tam<55):
        hash = rellenar(hash,0)
        print(hash)
        return hash





#Comienza el programa
def Iniciar(palabra):
    tam = len(palabra)
    palabra = tamaño(tam,palabra)
    a = b58(palabra)
    print("Mensaje codificado a base58: " + a)
    print("")
    print("Base58 a binario: ")
    print(toBinary(a))
    print("")
    arr = toBinary(a)
    X = ConvertXOR(arr)
    print("")
    pf=ConvertToASCII(X)
    print("Hash final en ASCII: ", pf)
    return pf

#Iniciar()

#Leer un archivo .txt y extraer una palabra por linea en formato de texto plano
def leerArchivo(a):
    archivo = open(a,"r")
    palabras = []
    for linea in archivo:
        print("Palabra n° ", len(palabras)+1)
        print(linea)
        pf = Iniciar(linea)
        print("==========================================================")
        palabras.append(linea)
    return pf


def leerArchivosinImprimir(a):
    archivo = open(a,"r")
    palabras = []
    for linea in archivo:
        palabras.append(linea)
    return palabras

#Calculo de hash de palabras en md5,sha1 y sha256 
def md5(palabras):
    hash = hashlib.md5(palabras.encode())
    print(hash)
    print("Hash de la palabra: ", hash.hexdigest())
    print("==========================================================")
    return hash.hexdigest()

def sha1(palabras):
    hash = hashlib.sha1(palabras.encode())
    print("Hash de la palabra: ", hash.hexdigest())
    print("==========================================================")
    return hash.hexdigest()

def sha256(palabras):
    hash = hashlib.sha256(palabras.encode())
    print("Hash de la palabra: ", hash.hexdigest())
    print("==========================================================")
    return hash.hexdigest()


#Calcular cantidad de caracteres de una palabra


