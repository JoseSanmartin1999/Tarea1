"""
Se desea realizar un programa que nos devuelva el valor mas alto de un exponente 
el cual al ser el exponente de 2 nos de N sin residuos. 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os, big_o

while(True):
        #Se crea un try para comprobar las condiciones 
        try:
        #Se pide que ingresamos una cadena de numeros 
            N=int(input("Ingrese el Numero N: "))
        #Se crea la expecion a la regla 
        except ValueError:
            #Se crea un mensaje de advertencia
            print("Debe ser un numero entero")
            #Si las condiciones son adecuadas se continua 
            continue
        #Condicion en la cual no podemos ingresar un numero negativo
        if N<0:
            #Creamos el mensaje de advertencia
            print("Debe ser un numero entero positivo")
            #Si se cumplen las condiciones se continua
            continue
        #en caso de que se cumple
        else:
            #Se sale del bucle 
            break
def solucion(N):
    """
     Es una funcion la cual toma un numero ingresado por el usuario y 
     mira que numero mayor elevado a un exponente da como residuo 0
    ------------
    N: Es el numero ingresado por el usuario para que sea analziado
           
    Retorna:
    ------------
      Retorna el exponente que cumple con la condicion
       """
    exponente=0
    division=N%(2**exponente)
    while division==0:
        exponente+=1
        division=N%(2**exponente)
    return exponente-1


if __name__ == '__main__':
    #Imprime el resultado     
    print ("el exponente  es",solucion(N))
    numero_sample=lambda example_variable:N
    best,others=big_o.big_o(solucion,numero_sample)
    print(best)
#Se saldra del programa con un click
os.system("Pause")