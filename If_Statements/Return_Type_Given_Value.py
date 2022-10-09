# -*- coding: utf-8 -*-
#Program : Return type given value
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def which_type(val):        #define a function called which type
    val= type(val)          #asign in the variable "val" the type of the variable "val"
    if(val == bool ):       #cicle if, compares if  val contains a type boolean
        z="boolean"         #asign "boolean" to "z"
        print(z)            #print value contains in z
    elif(val== float):      #cicle if, compares if val contains a type float
        z="float"           #asign "float" to "z"
        print(z)            #print value contains in z
    elif( val == int):      #cicle if, compares if val contains a type integer
        z="integer"         #asign "integer" to "z"
        print(z)            #print value contains in z
    elif(val == str):       #cicle if, compares if val contains a type string
        z="string"          #asign "string" to "z"
        print(z)            #print value contains in z
    return z                #return the value contains in z

which_type("hola")