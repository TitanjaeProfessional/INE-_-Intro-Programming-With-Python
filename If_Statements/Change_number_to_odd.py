# -*- coding: utf-8 -*-
#Program :  Change number to odd 
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def make_number_odd(number):    #define a function name make number odd
    if(number % 2 == 0):        #cicle if , verify if module from number/2 is 0
       number=number+1          # numbe add it "1
    return number

make_number_odd(2)
