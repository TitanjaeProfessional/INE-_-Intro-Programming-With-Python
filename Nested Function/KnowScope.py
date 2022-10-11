# -*- coding: utf-8 -*-
#Program :Know Scope
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 11  2022

#Analyze the following code and answer: What will be the final value of c after the execution of this code:

a = 10
b = 3
c = 7
def test_scope(b):
    a = 11
    return a + b + c

c = c + test_scope(5)


#the value of c is 30 
