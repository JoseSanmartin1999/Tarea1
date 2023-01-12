"""
Se desea realizar un programa en el que al ingresar una cadena de caracteres de cualquier
tipo nos devolvera el indie medio de esta caso contrario nos debe dar -1

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#importamos las bibliotecas que iremos a usar 
import math,big_o
 #ingresamos la cadena a analizar
palabra=input("Ingresar una palabra: ")
def solucion(palabra):
    """
     Es una funcion la cual toma una cadena de caracteres para encontar su indice medio
     en caso de que este exista es decir la palabra o cadena sea impar nos devuelve la 
     cadena de strings previa y continua de la mitad de la cadena 
    Recibe:
    ------------
      cadena:Es la cadena de caracteres que se va a recibir 
           
    Retorna:
    ------------
       respuesta: Retorna el numero de substrings creados 
    """
   
    #buscamos devolver la longitud de la cadena 
    longitud=len(palabra)
    #mientras el residuo de la division sea igual a 0 
    if longitud%2 ==0:
        #imprimos el resultado de la condición
       return -1
       #en caso de que la division de la longtiud sea diferente de 0
    elif longitud%2 !=0:
        #Tomamos la longitud y la redondeamos para saber los caracteres 
        respuesta=math.floor(longitud/2)
        #Creamos la condicion en caso de que al respuesta sea 0 
        if respuesta ==0:
            #imprimos la opcion
            return -1
            #en caso contrario se vamos a pedir que se imprima la variable r 
        else:
            #se imprime r 
            return respuesta
    



if __name__ == '__main__':
    #Imprime el resultado
    print("la cantidad de caracteres en el substring es: ",solucion(palabra))
    cadenapalabra_sample=lambda example_variable:palabra
    best,others=big_o.big_o(solucion,cadenapalabra_sample)
    print(best)