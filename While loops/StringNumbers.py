# -*- coding: utf-8 -*-
#Program :string of number
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022

def string_of_numbers(a):           #define a function called string of numbers
    number_str=""                   #define a value empty for string
    count=1                         #asing 1 to count
    while count<a+1:                #cicle while, where count be less than a+1  
        number_str+=str(count)      #asign and add a string for the count numbers
        count+=1                    #asign and add 1 to the count
    print(number_str)               #print the value contains in number_str
    return number_str               #return the value contains in number_str
    
string_of_numbers(5)
        