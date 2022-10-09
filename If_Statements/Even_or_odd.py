# -*- coding: utf-8 -*-
#Program : Ever or odd
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def even_or_odd(a_number):  #Define a function called even or odd
    if(a_number%2 == 0):    #cicle if, compares if a module from "a_number"/2 is equal to 0
        print("even")       #print even
    elif(a_number%2 != 0):  #cicle elif, compares if a module from "a_number"/2 is different to 0
        print("odd")        #print odd
        
even_or_odd(5)