# -*- coding: utf-8 -*-
#Program :  Condition multiplication
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def conditional_multiplication(a_condition, number):    #Define function with parameters condition and number
    if( a_condition == True):                           #cicle if where "a_condition" == True
        number=number*10                                #multiply the number save in variable number plus 10 and save it in the same variable
        print(number)                                   #print the value asign in number
    elif(a_condition == False):                         #cicle if where "a_condition" == False
        number=number                                   #variable number continue with the same value
        print(number)                                   #print the value asign in number
    return number                                       #return the value contains in number


