# -*- coding: utf-8 -*-
#Program :double number
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 10  2022

def double_down(num, times_doubled):        #define a function called DOuble down
    count=0                                 #asign a initial position for count
    while count < times_doubled:            #cicle while , where count must be less than times doubled
        num*=2                              #asign and plus 2 to the number contains into num
        count+=1                            #asign and add a 1 to count
    return num                              #return the value contains in num

print(double_down(3, 3 ))