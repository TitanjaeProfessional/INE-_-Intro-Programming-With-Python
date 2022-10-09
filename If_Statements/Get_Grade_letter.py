# -*- coding: utf-8 -*-
#Program :  Get a grade letter
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def get_grade_letter(score):            #Define a function called get a grade letter
    if((score>=90)):                    #cicle if, where codition is score bigger than 90
        return 'A'                      #return "A"
    elif((score>=80) and (score<=89)):  #cicle else if, where condition is score must be into a range 80-89
        return 'B'                      #return "B"
    elif((score>=70) and (score<=79)):  #cicle else if, where condition is score must be into a range 70-79
        return 'C'                      #return "C"
    elif((score>=60) and (score<=69)):  #cicle else if, where condition is score must be into a range 60-69
        return 'D'                      #return "D"
    elif((score< 60)):                  #cicle else if, where condition is  score less than 60
        return 'F'                      #return "F"