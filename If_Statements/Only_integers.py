# -*- coding: utf-8 -*-
#Program : only integers
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022


def add_only_integers(a, b):                        #Define a function called add only integers
    value1type=type(a)                              #verify type of a
    value2type=type(b)                              #verify type of b
    if((value1type==int) and (value2type==int)):    #cicle if, where condition is a and b are int
        z=a+b                                       #asign add to z
        print(z)                                    #print the value contains in z
        return z                                    #return the value contains in z
    else:                                           #cicle else, without condition
        print("invalid parameter")                  #print a text "invalid parameter"
        
add_only_integers(2, 'what')    
add_only_integers(2, 3)