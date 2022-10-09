# -*- coding: utf-8 -*-
#Program :  Greatter parameter
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022

def greatest_parameter(a, b, c, d, e):  #Define a function called greatest parameter
    listaval = (a,b,c,d,e)              #save the values a,b,c,d,e into a list
    gp=a                                #asign a to gp
    for i in range(5):                  #cicle if, where i must repeat 5 times
        if(gp<listaval[i]):             #cicle if, where condition is if gp is less than listaval in position define for i
            gp=listaval[i]              #if cicle if be correct, gp saves value where be in postion listaval[i]
    print(gp)                           #print value contains in gp
    return gp                           #return the value contains in gp

greatest_parameter(2, 4, 9, 1, 1)
greatest_parameter(42, 4, 9, 1, 1)
greatest_parameter(5, 4, 9, 1, 17)


        