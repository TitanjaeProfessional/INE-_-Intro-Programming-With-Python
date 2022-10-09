# -*- coding: utf-8 -*-
#Program :All string? 
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def all_strings(a, b, c):                   #define a function called all string
    d=type(a)                               #asign into variable "d" the type of structure correspond it to "a"
    e=type(b)                               #asign into variable "e" the type of structure correspond it to "b"
    f=type(c)                               #asign into variable "f" the type of structure correspond it to "c"
    if((d==str) and (e==str) and(f==str)):  #cicle if, compares if variables d,e and f correspond to a string
        z=True                              #asign true in "z"
        print(z)                            #print the value contains in z
        return z                            #return the value contains in z
    else:                                   #cicle else,without condition
        z=False                             #asign false in "z"
        print(z)                            #print the value contains in z
        return z                            #return the calue contains in z

all_strings("f", "s", "a")



