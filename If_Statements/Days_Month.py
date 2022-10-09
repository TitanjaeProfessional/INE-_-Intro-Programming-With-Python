# -*- coding: utf-8 -*-
#Program :  When you can never remember how many days each month has
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022

def how_many_days_in(a_month):  #Define a function name hoy many days
    if ( (a_month=='January') or (a_month=='March') (a_month=='May') or (a_month=='July') or (a_month=='August') or (a_month=='October') or (a_month=='December')):
        z=31                    #asign 31 to z
    elif((a_month=='April')or(a_month=='June')or(a_month=='September')or(a_month=='November')):
        z=30                    #asign 30 to z
    elif((a_month=='February')):
        z=28                    #asign 28 to z
    return z                    #return the value asign to z
