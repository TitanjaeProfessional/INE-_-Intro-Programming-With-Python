# -*- coding: utf-8 -*-
#Program :  Calculator
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Cretaed on Mon Oct 4  2022
import math

def add():                                                  #We define a function add 
    cantidad = int(input("Dame la cantidad de numeros"))    #we difine quantitiy of numbers we would want to substract
    listanum=[]                                             #We create an empty list to upload de values
    listaNumeros(listanum,cantidad)                         #We call the function listaNumeros
    addprocess= sum(listanum)                               #we add all the values in the listnum using the word sum
    return addprocess                                       #return the result of add process

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
    return multiplyprocess                                  #return the result of multiplay process


def divide():                                               #We define a function divide
    a=int(input("Dame el primer numero"))                   #We request the value of a
    b=int(input("Dame el segundo numero"))                  #We request the value of b
    if ((b == 0)):                                          #We difine a case where denominator be 0
       return print("You can't divide a number by 0")       #You can'tt divide a number by 0 
    elif((a == 0)):                                         #We difine the oposite case where numerator be 0
        z=0                                             
        return z                                            #We only return a 0 
    else:                                                   #In the case like the other ifs does not apply , this case happens. a comun division
        DivideProcess= a/b
        return DivideProcess                                #return the result of divide process

def SquareNumber():                                        #We difine a fucntion to square a number
    a=int(input("Dame el primer numero"))                   #We request the value of a
    SquareNumberprocess =a**2                               #We pow a number to them square form
    return SquareNumberprocess                              #return yhe result of square process

def PowerNumber():                                       #we difine a function to power a number by anothe number ask
    a=int(input("Dame el primer numero"))                   #We request the value of a
    b=int(input("Dame el segundo numero"))                  #We request the value of b
    PowerNumberProcess= pow(a, b)                           #we pow a number to them another number
    return PowerNumberProcess                               #we return the result from powernumberprocess

def SquareRoot():                                          #we define a function to get the square root
    a=int(input("Dame el primer numero"))                   #We request the value of a
    SquareRootProcess= math.sqrt(a)                         #using the library math we get the square root by the word (sqrt)
    return SquareRootProcess                                #we return the result from squarerootprocess

def listaNumeros(listanum,cantidad):                        #we define a list where we gonna put the numbers for the function add, substract and multiply
    while cantidad >0:                                      #we use while to specific that if cantidad dont be less than 0 the cicle into the while continue execute
        dato = int(input("Dame le numero"))                 #we ask for the number we would put in the list
        listanum.append(int(dato))                          #we add that number to the list
        cantidad-=1                                         #we susbtract 1 to the number cantidad an save it in the same variable
    print(listanum)                                         #we print the list listnum
    return listanum                                         #we return the list listnum

def CalculadoraExecute():
    print("Bienvenido al archivo calculadora")
    print("Tenemos las siguientes opciones") 
    print("1.- Suma")
    print("2.- resta")
    print("3.- multiplicacion")
    print("4.- division")
    print("5.- Numero al cuadrado")
    print("6.- Numero a la potencia de otro numero")
    print("7.- Raiz cuadrad")
    print("Selecciona alguna de las opciones colocando el numero de la opcion")
    opcionCalculadora =int(input("Num opcion : "))
    if opcionCalculadora ==1:
        print(add())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora ==2:
        print(substract())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora ==3:
        print(multiply())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora ==4:
        print(divide())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora==5:
        print(SquareNumber())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora==6:
        print(PowerNumber())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    elif opcionCalculadora==7:
        print(SquareRoot())
        print("¿Ya has acabado de utilizar el programa")
        valueanswer =input("y/n :")
        if valueanswer == 'n':
            CalculadoraExecute()
        elif valueanswer == 'y':
            exit()
    else:
        print("Esa opcion no existe")
        CalculadoraExecute()
    return 

CalculadoraExecute()