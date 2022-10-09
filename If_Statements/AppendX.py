# -*- coding: utf-8 -*-
#Program :  Append X
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def append_x(a_string):             #define a function calle append x
    if(a_string != ""):             #cicle if, verify if a_string is not empty
        a_string = a_string +"x"    #asign to a_string  the value a_string+ string "x"
        print(a_string)             #print the value contains in a_string
    else:                           #cicle else, without condition
        a_string = a_string         #save into a_string the same value
        print(a_string)             #print the value contains in a_string
    return a_string                 #return the value contains in a_string

append_x("")