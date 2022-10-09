# -*- coding: utf-8 -*-
#Program :  Greatter than
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def greater_than_20(number):    #define a function called greater than 20
    if (number < 20):           #cicle if, compares number less than 20
        z= False                #asign false to z 
        print(z)                #print the value contains in z
    elif (number >20):          #cicle if, compares number greater than 20
        z= True                 #asign true to z
        print(z)                #print the value contains in z
    return z                    #return the value contains in z 

greater_than_20(21)