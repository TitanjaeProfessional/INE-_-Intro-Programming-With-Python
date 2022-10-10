# -*- coding: utf-8 -*-
#Program :Fix this code: interest
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022


#fix the following code:

def compound_interest_result1(initial_investment1, interest_percentage1, num_periods1):
    total = initial_investment1
    count = 0
    while count < num_periods1:
        total += initial_investment1 * .1
        count += 1
    return total
print(round(compound_interest_result1(1000, 10, 5), 2))
#Code fixed

def compound_interest_result(initial_investment,interest_percentaje,num_periods):   #define function called compund interest result
    inicial=initial_investment                                                      #asign the initial investmetn to variable inicial
    percentaje=(1/(interest_percentaje))                                            #asign in to percentaje  1/interest_percentaje with the objetive to change to percentaje
    count=0                                                                         #define the first position for the count
    if(num_periods == 0):                                                           #cicle if, where contidition is num periods be "0" return the same value of inicial
        return inicial                                                              #return the value contains in inicial
    elif (num_periods == 1):                                                        #cicle if, where codition is num periods be "1" return the interest add to the initial value                 
        inicial+=inicial*percentaje                                                 #Inicial asign be the value contains in inicial add the interest       
        return inicial                                                              #return the value contains in inicial
    elif (num_periods>1):                                                           #cicle if, where condition is num periods be bigger than "1"
        x=inicial*percentaje                                                        #the line 30 to line 34 corresponds to the calculte to add the interest to the value depending the num of periods
        inicial+=inicial*percentaje
        while count < num_periods-1:
            x+=x*percentaje
            inicial+=x
            count+=1                                                                #add 1 to the count
        return inicial                                                              #return the value asign to inicial

print(round(compound_interest_result(1000, 10, 2), 2))