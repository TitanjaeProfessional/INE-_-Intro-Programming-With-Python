# -*- coding: utf-8 -*-
#Program :Help a String Get Lucky 
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022

def get_lucky(poor_string, lucky_number):   #Define a function called get lucky
    count= 0                                #asign a inititate value to count
    while count < lucky_number:             #cicle while, where condition is count less than lucky number
        poor_string=poor_string+"7"         #asign and add to variable poor string a string "7"
        count+=1                            #asign and add a 1
    print(poor_string)                      #print the value contains in "poor string"
    
get_lucky("rabbit foot", 3)
get_lucky("shiny penny", 5)