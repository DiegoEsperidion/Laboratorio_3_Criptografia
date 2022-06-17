from hash import Iniciar, leerArchivo , leerArchivosinImprimir , md5,sha1,sha256,entropia,md5solo,sha1solo,sha256solo
import time

def main():
    print("Seleccione el archivo a leer: ")
    print(" ")
    print("1. 1 caracter")
    print("2. 10 caracteres")
    print("3. 20 caracteres")
    print("4. 50 caracteres")
    print("5. Otro método de hash")
    print("6. Ingresar una palabra")

    d= input()

    if(d=="1"):
        Inicio=time.time()
        leerArchivo("1.txt")
        Termino=time.time()
        print("Tiempo de ejecucion: ", Termino-Inicio)
        return 0
    elif(d=="2"):
        Inicio=time.time()
        leerArchivo("10.txt")
        Termino=time.time()
        print("Tiempo de ejecucion: ", Termino-Inicio)
        return 0
    elif(d=="3"):
        Inicio=time.time()
        leerArchivo("20.txt")
        Termino=time.time()
        print("Tiempo de ejecucion: ", Termino-Inicio)
        return 0
    elif(d=="4"):
        Inicio=time.time()        
        leerArchivo("50.txt")
        Termino=time.time()
        print("Tiempo de ejecucion: ", Termino-Inicio)
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
            print("Seleccione el archivo a leer en md5: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            print("5. Ingresar una palabra")
            d= input()

            if(d=="1"):
                Inicio=time.time()
                md5(leerArchivosinImprimir("1.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="2"):
                Inicio=time.time()
                md5(leerArchivosinImprimir("10.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="3"):
                Inicio=time.time()
                md5(leerArchivosinImprimir("20.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="4"):
                Inicio=time.time()
                md5(leerArchivosinImprimir("50.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="5"):
                print("Ingrese la palabra a calcular: ")
                pal= input()
                Inicio=time.time()
                md5solo(pal)
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)

            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="2"):
            print("Seleccione el archivo a leer en sha1: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            print("5. Ingresar una palabra")
            d= input()


            if(d=="1"):
                Inicio=time.time()
                sha1(leerArchivosinImprimir("1.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="2"):
                Inicio=time.time()
                sha1(leerArchivosinImprimir("10.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="3"):
                Inicio=time.time()
                sha1(leerArchivosinImprimir("20.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="4"):
                Inicio=time.time()
                sha1(leerArchivosinImprimir("50.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="5"):
                print("Ingrese la palabra a calcular: ")
                pal= input()
                Inicio=time.time()
                sha1solo(pal)
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="3"):
            print("Seleccione el archivo a leer en sha256: ")
            print(" ")
            print("1. 1 caracter")
            print("2. 10 caracteres")
            print("3. 20 caracteres")
            print("4. 50 caracteres")
            print("5. Ingresar una palabra")
            d= input()

            if(d=="1"):
                Inicio=time.time()
                sha256(leerArchivosinImprimir("1.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="2"):
                Inicio=time.time()
                sha256(leerArchivosinImprimir("10.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="3"):
                Inicio=time.time()
                sha256(leerArchivosinImprimir("20.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="4"):
                Inicio=time.time()
                sha256(leerArchivosinImprimir("50.txt"))
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            elif(d=="5"):
                print("Ingrese la palabra a calcular: ")
                pal= input()
                Inicio=time.time()
                sha256solo(pal)
                Termino=time.time()
                print("Tiempo de ejecucion: ", Termino-Inicio)
            else:
                print("Intentelo de nuevo")
                main()
                return 0
        elif(e=="4"):
            return 0
    elif(d=="6"):
        print("Ingrese palabra a hashear")
        palabra=input()
        Inicio=time.time()
        entropia(Iniciar(palabra))
        Termino=time.time()
        print("Tiempo de ejecucion: ", Termino-Inicio)

               

main()


