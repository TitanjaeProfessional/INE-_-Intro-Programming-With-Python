# -*- coding: utf-8 -*-
#Program : Traffic light 
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def traffic_light(color):       #define a function called traffic light
    if(color == "green" ):      #cicle if, Conditional if color is equal to "green"
        return 'go'             #return "go"
    elif(color == "red"):       #cicle if, Conditional if color is equal to "red"
        return 'stop'           #return " stop"
    elif(color == "yellow"):    #cicle if, Conditional if color is equal to "yellow"
        return 'slow down'      #return "slow down"

traffic_light("green")