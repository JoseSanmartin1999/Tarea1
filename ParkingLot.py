"""
Se desea realizar un programa que simule un parqueadero y el cobro de esto por el tiempo que 
el vehiculo estuvo en el parqueadero 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#se importa las librerias necesarias 
import datetime, os,big_o
#esta variable indica el precio por entrar al parqueadero
entrada=2
#esta variable indica el precio por la primera hora o parcual en el parqueadero
primerahoraopar=3
#esta variable indica el precio por estar mas de una hora en el parqueadero
masdeunahora=4
#Limita el numero de caracteres que va a tomar el input
limite=5  
#Ingresa la hora de entrada que el usuario desee   
hentrada=(input("Ingresar hora de entrada HH:MM  :")[:limite])
#Ingresa la hora de salida que el usuario desee  
hsalida=(input("Ingresar hora de salida HH:MM  :")[:limite])   

def Solution(limite):
    """
     Es una funcion la cual toma las horas de ingreso y salida del vehiculo
     realiza las operaciones correspondientes al cobro 
     Recibe
    ------------
      limite: limita la cantidad de caracteres que se ingresan
           
    Retorna:
    ------------
       precio_a_pagar: Retornar el precio a pagar 
    """
    #Limita el numero de caracteres que va a tomar el input
    
    #Ingresa la hora de entrada que el usuario desee         
    #hentrada=(input("Ingresar hora de entrada HH:MM  :")[:limite])
    #toma los dos primeros caracteres de la cadena y los convierte en enteros 
    H1=int(hentrada[0:2])
    #toma los dos ultimos caracteres de la cadena y los convierte en enteros 
    M1=int(hentrada[3:5])
    #Se pone un condicion para que los valores ingresados por puedan ser mayores a 23 horas o 59 minutos 
    if (H1>=0 and H1<=23) and (M1>=0 and M1<=59):
        #Se copila y se mantiene el dato de entrada de un vehiculo
        entra=datetime.timedelta(hours= H1 , minutes=M1)
        
        #toma los dos primeros caracteres de la cadena y los convierte en enteros 
        H2=int(hsalida[0:2])
        #toma los dos ultimos caracteres de la cadena y los convierte en enteros 
        M2=int(hsalida[3:5])
         #Se pone un condicion para que los valores ingresados por puedan ser mayores a 23 horas o 59 minutos 
        if(H2>=0 and H2<=23) and (M2>=0 and M2<=59):
        #Se copila y se mantiene el dato de salida de un vehiculo
            sal=datetime.timedelta(hours= H2 , minutes=M2)
        #Se calcular el tiempo total dentro del parqueadero de vehiculo
            horastotal=sal-entra
        #Se calcula el tiempo en horas totales dentro del parqueadero
            H3=int(H2-H1)
        #Se calcula el tiempo en minutos totales dentro del parqueadero
            M3=int(M2-M1)
       
        else:
            #Se imprimer el mensaje en advertencia 
            print("No existe, La hora minima es 00:00 y la Maxima 23:59")
            #Se regresa al checkpoint 
            return Solution()
    #Se imprimer el mensaje en advertencia 
    else:
          #Se imprimer el mensaje en advertencia 
        print("No existe, La hora minima es 00:00 y la Maxima 23:59")
        #Se regresa al checkpoint 
        return Solution()

    #Se crea un condiicion para cuando se estuvo solo una hora y un poco mas dentro del parqueadero   
    if H3==1 and M3==0:
        precio_a_pagar=entrada+primerahoraopar
         #Se imprime el total a pagar 
        return precio_a_pagar
    #Se crea un condiicion para cuando se estuvo solo minutos dentro del parqueadero       
    elif H3==1 and M3!=0:
         #Se calcula el precio a pagar
        precio_a_pagar=entrada+primerahoraopar+masdeunahora
         #Se imprime el total a pagar 
        return precio_a_pagar
    #Se crea un condiicion para cuando se estuvo solo minutos dentro del parqueadero  
    elif H3==0 and M3>=0:
         #Se calcula el precio a pagar
        precio_a_pagar=entrada+primerahoraopar
        return precio_a_pagar
        #Se crea un condiicion para cuando se estuvo mas de una hora y alguno minutos mas  
    elif H3>1 and M3!=0:
        horasTotales=round((M3/60)+H3)
         #Se calcula el precio a pagar
        precio_a_pagar=entrada+primerahoraopar+(horasTotales*masdeunahora)
        return precio_a_pagar
        #Se crea un condiicion para cuando se estuvo solo una hora en el parqueadero 
    elif H3>1 and M3==0:
        #Se calcula las horas totales
        horasTotales=round((H3-1))
         #Se calcula el precio a pagar
        precio_a_pagar=entrada+primerahoraopar+(horasTotales*masdeunahora)
        return precio_a_pagar
       

if __name__ == '__main__':
    #Imprime el resultado
    print("el precio a pagar es: $",Solution(limite))
    limite_sample=lambda example_variable:limite
    best,others=big_o.big_o(Solution,limite_sample)
    print(best)
    #Se saldra del programa con un click
    os.system("Pause")

   

  
    

