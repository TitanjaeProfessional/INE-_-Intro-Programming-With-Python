# -*- coding: utf-8 -*-
#Program : Prueba Funciones Calculadora
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Cretaed on Mon Oct 4  2022


#Listanum = []
#cantidad = int(input(("cuantos datos vas a ingresar")))
#while cantidad>0:
   # dato = int(input("Dame le numero"))
  #   cantidad-=1
#print("contenido de la lista  = ",Listanum)
def listaNumeros(listanum,cantidad):
    while cantidad >0:
        dato = int(input("Dame le numero"))
        listanum.append(int(dato))
        cantidad-=1
    print(listanum)
    return listanum

def substract():                                            #We define a function substract
    cantidad = int(input("Dame la cantidad de numeros"))    #we difine quantitiy of numbers we would want to substract
    listanum=[]                                             #We create an empty list to upload de values
    listaNumeros(listanum,cantidad)                         #We call the function listaNumeros
    substractprocess=listanum[0]                            #We difine susbtractionprocces in the position number[0] of the listnum to substract the other numbers
    for a in range(cantidad-1):                             #We difine a for cicle  where (a) must be the value to increment the count an position who will substract the numnber  and (cantidad-1) must be the limit of the cicle for
          substractprocess= substractprocess-listanum[a+1]  #We difine en substraccionprocces to the substract position listnum[0] and position (a+1)  who start in postion listnum[1] and have and increment depending the cicle for
    return substractprocess                                 #return the result of substract process



def multiply ():                                            #We define a function multiply
    cantidad = int(input("Dame la cantidad de numeros"))    #we difine quantitiy of numbers we would want to substract
    listanum=[]                                             #We create an empty list to upload de values
    listaNumeros(listanum,cantidad)                         #We call the function listaNumeros
    multiplyprocess=listanum[0]                             #We difine multyproccess in position number 0 from listnum
    for i in range(cantidad-1):                             #We difine a for cicle  where (i) must be the value to increment the count an position who will multiply the numnber  and (cantidad-1) must be the limit of the cicle for
        multiplyprocess=multiplyprocess*listanum[i+1]       #We difine in multiplyprocess the multiplication in  position listnum[0] and position (a+1)  who start in postion listnum[1] and have and increment depending the cicle for
    return multiplyprocess  

print(multiply())