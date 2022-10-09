# -*- coding: utf-8 -*-
#Program : Is a String?
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def is_string(variable):        #define function called  is string
    variable = type(variable)   #verify what cain of type structure is the variable "variable"
    if (variable == str):       #cicle if, Compares if type corresponds to a string
        z=True                  #asign true to "z"
        print(z)                #print the value contains in z
    else:                       #cicle else, without condition
        z=False                 #asign false to "z"
        print(z)                #print the value contains in z
    return z                    #return the value contains in z

is_string(2)