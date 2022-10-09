# -*- coding: utf-8 -*-
#Program :  Is numeric?
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def is_numeric(a_number):               #define a function called is numeric
    x=type(a_number)                    #Save in variable "x" the type structure of "a_number"
    if((x ==  int) or (x == float)):    #cicle if, compares if "x" is integer or float
        z=True                          #asign "true" in "z"
        print(z)                        #print the value contains in z
    else:                               #Cicle else, without condition
        z=False                         #asign "false" in z
        print(z)                        #print the value contains in z
    return z                            #returns the value contains in z

is_numeric(3.12)