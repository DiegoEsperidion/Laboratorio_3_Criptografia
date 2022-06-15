from hash import leerArchivo , leerArchivosinImprimir , md5,sha1

def main():
    print("Seleccione el archivo a leer: ")
    print(" ")
    print("1. 1 caracter")
    print("2. 10 caracteres")
    print("3. 20 caracteres")
    print("4. 50 caracteres")
    print("5. Otra cosa")

    d= input()

    if(d=="1"):
        leerArchivo("1.txt")
        return 0
    elif(d=="2"):
        leerArchivo("10.txt")
        return 0
    elif(d=="3"):
        leerArchivo("20.txt")
        return 0
    elif(d=="4"):
        leerArchivo("50.txt")
        return 0
    elif(d=="5"):
        print("Ingrese si desea calcular con md5 ,sha1 o sha256: ")
        print("1. md5")
        print("2. sha1")
        print("3. sha256")
        print("4 Terminar")
        e= input()
        print("")
        if(e=="1"):
            print("Seleccione el archivo a leer: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            d= input()

            if(d=="1"):
                md5(leerArchivosinImprimir("1.txt"))
            elif(d=="2"):
                md5(leerArchivosinImprimir("10.txt"))
            elif(d=="3"):
                md5(leerArchivosinImprimir("20.txt"))
            elif(d=="4"):
                md5(leerArchivosinImprimir("50.txt"))
            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="2"):
            print("Seleccione el archivo a leer: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            d= input()


            if(d=="1"):
                sha1(leerArchivosinImprimir("1.txt"))
            elif(d=="2"):
                sha1(leerArchivosinImprimir("10.txt"))
            elif(d=="3"):
                sha1(leerArchivosinImprimir("20.txt"))
            elif(d=="4"):
                sha1(leerArchivosinImprimir("50.txt"))
            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="3"):
            print("Seleccione el archivo a leer: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            d= input()

            if(d=="1"):
                sha256(leerArchivosinImprimir("1.txt"))
            elif(d=="2"):
                sha256(leerArchivosinImprimir("10.txt"))
            elif(d=="3"):
                sha256(leerArchivosinImprimir("20.txt"))
            elif(d=="4"):
                sha256(leerArchivosinImprimir("50.txt"))
            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="4"):
            return 0
    else:
        return 0
               

main()


