# -*- coding: utf-8 -*-
#Program :  Change number to odd binary
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022


def convert_bool_to_binary(a_boolean):  #define function name convert bool to binary
    if(a_boolean == True):              #cicle if, compare value in "a_boolean" be equal to true
        number= 1                       #asign "1" to variable "number"
        print(number)                   #print the value contains in number
    elif(a_boolean == False):           #cicle if, compare value in "a_boolean" be equal to false
        number=0                        #asign "0" to variable "number"
        print(number)                   #print the value contains in number
    return number                       #return the value contains in number

convert_bool_to_binary(False)