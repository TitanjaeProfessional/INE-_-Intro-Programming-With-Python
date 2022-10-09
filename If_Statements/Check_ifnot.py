# -*- coding: utf-8 -*-
#Program :Check if none
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def check_if_none(a, b, c, d, e):                                       #define function called check if none
    if((a==None) or (b==None) or (c==None) or (d==None) or (e==None)):  #Cicle if , Conditional if anyone of the variables its equal to NONE
        z=True                                                          #asign true to z
        print(z)                                                        #print the value contains in z
        return z                                                        #return the value contains in z
    else :                                                              #cicle else, without condition
        z=False                                                         #asign false to z
        print(z)                                                        #print the value contains in z
        return z                                                        #return the value contains in z
    

    