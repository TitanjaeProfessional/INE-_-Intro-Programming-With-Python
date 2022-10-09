# -*- coding: utf-8 -*-
#Program :  Check divisibility
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

divisible_by_11 = 11                        #Asign "11" to "devisible_11"

is_583_divisible_by_11 = None               #Asign value None to the variable
is_911_divisible_by_11 = None               #Asign value None to the variable

number_583 = 583                            #Asign "583" to "number_583"

if number_583 % divisible_by_11 == 0:       #Cicle for , comparing the result from module 
    is_583_divisible_by_11 = True           #Asign value true to "is_583_divisible_by_11"
else:
    is_583_divisible_by_11 = False          #Asign value false to "is_583_divisible_by_11"


is_911_divisible_by_11 = None               #Asign value None to "is_911_divisible_by_11"
number_911 = 911                            #Asign "911" to "number_911"

if number_911 % divisible_by_11 == 0:       #Cicle for , comparing the result from module 
    is_911_divisible_by_11 = True           #Asign value true to "is_911_divisible_by_11"
else:
    is_911_divisible_by_11 = False          #Asign value true to "is_911_divisible_by_11"

print(is_583_divisible_by_11)               #print the value contain in "is_583_divisible_by_11"
print(is_911_divisible_by_11)               #print the value contain in "is_911_divisible_by_11"