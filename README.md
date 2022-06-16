# Instrucciones

El proceso para hashear un texto plano se representa mediante el diagrama subido en el ithub (lab3.png), el proceso es el siguiente:

1.- Selecciona un texto de entrada, el cual puede ser cualquier digito que este implementado en el teclado , el programa lo trnasformara posteriormente a base58, en el caso que sea un archivo de texto, el programa tiene la funcion de leerlo linea por linea para extraer los datos.

1.1.- Las palabras deben ser iguales a 40, en caso contrario el programa se encarga de rellenar con ua secuencia definida para cumplir con el requisito (de esta forma al pasarlo a base58 nos entrega un valor exacto de 55 caracteres)

2.- Una vez tenemos la base, transformamos el texto plano en binario

3.- Se aplica un XOR en base a la password y una llave que es definida en el codigo (1011101)

4.- Transformar en ASCII para retornar finalmente el valor de Hash (el valor retorna en forma byte, por lo que finalmente se hace conversion de bytes a string para asi luego calcular su entropia.)


# Adicional

La forma para visualizar lo mencionado en un esquema, se encuentra en el archivo **Lab3.png**
[Imagen](Laboratorio_3_Criptografia/Lab3.png)

Todas las funciones que realizan este proceso se encuentran en el archivo **hash.py** y el codigo que es necesario para ejecutarlo es el archivo **decision.py**.

Por ultimo la entropia se implemento en el archivo **entropia.py** y en este caso se implemento el uso de comprobar manualmente si la entropia cambia respecto a una palabra u otra (SPOILER: no), lo unico que hay que hacer es ir  cambiando la variable "pal" y a comparar.

Como agregado adicional, si se desea ver todo el proceso funcionando y sin necesidad de ejecutarlo, a continuacion se encuentra un enlace que lo redirigirá a un video de youtube explicando todo el proceso.

[Video Youtube](https://youtu.be/O0ZtRBe5IGk)

