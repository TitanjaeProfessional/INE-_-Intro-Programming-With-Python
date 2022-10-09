# -*- coding: utf-8 -*-
#Program :Check out the boundaries
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def check_out_of_boundaries(number):    #Define a function called chek out of boundaries
    if ((number>0) and (number<10)):    #cicle if, conditional  where define a range like number be bigger than 0 but less than 10
        return False                    #return false           
    else:                               #cicle else, without condition
        return True                     #return true