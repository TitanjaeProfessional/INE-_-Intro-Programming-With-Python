# -*- coding: utf-8 -*-
#Program :Fix this code: legal age 
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 9  2022


#functional but it need to change it else to elif
def legal_ageunfix(age):
    if age > 21:
        return "You can do anything"
    else:
        if age == 21:
            return "You can do anything"
        else:
            if age > 18:
                return "You can drive with parents' permission"
            else:
                if age == 18:
                    return "You can drive with parents' permission"
                else:
                    if age == 17:
                        return "You'll have to wait"
                    else:
                        return "You'll have to wait"

#fix it

def legal_age(age):
    if(age > 21):
        return "You can do anything"
    elif (age == 21):
        return "You can do anything"
    elif (age > 18):
        return "You can drive with parents' permission"
    elif (age==18):
        return "You can drive with parents' permission"
    elif (age==17):
        return "You'll have to wait"
    else:
        return "You'll have to wait"
        
        