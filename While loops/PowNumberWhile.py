# -*- coding: utf-8 -*-
#Program :The Power of While Loops
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 10  2022



def  feel_the_power(initial_number, power):         #define a function called fell the power
    count=0                                         #asign a initial position for count
    if power == 0:                                  #cicle if ,where condition is power be equal to 0
        x=1                                         #asign 1 to "x"
        return x                                    #return the value contains in 1
    else:                                           #cicle else, withoun condition
        z=1
        while count < power:                        #cicle while , where count must be less than power -1
            z=z*initial_number                      #asign and plus initial number to the number contains into initial number
            count+=1                                #asign and add a 1 to count
        return z                                    #return the value contains in initial number

print(feel_the_power(2, 4))