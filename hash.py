import base58 # Se usa la libreria base58 para convertir el texto plano en base58
import binascii #libreria para convertir el XOR obtenido en binario en ASCII
#Ingresamos la palabra a codificar en base58


#Transformar a Base58
def b58(hash):
    a = base58.b58encode(hash.encode()).decode() 
    return a


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


print("Ingrese el hash a codificar: ")
hash = input()
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





#a = X[0][2:]
#a = int(a ,2)
#print(bin(a))
#print(a)
#
#print(binascii.unhexlify('%x' % a))









#Implement XOR of two binary numbers


