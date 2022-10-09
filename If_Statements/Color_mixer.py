# -*- coding: utf-8 -*-
#Program :Color mixer
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

def color_mixer(color1, color2):                                                                        #define a function called color mixer
    if (((color1=="yellow") or (color1=="red")) and ((color2 == "red") or (color2 == "yellow"))):       #cicle if, conditional where colors be red or yellow
        return 'Orange'                                                                                 #return 'orange'
    elif (((color1 == "blue") or (color1 == "yellow")) and ((color2=="blue") or (color2== "yellow"))):  #cicle if, conditional where colors be blue or yellow
        return 'Green'                                                                                  #return 'Green'
    elif(((color1=="blue")or(color1=="red")) and ((color2=="blue") or (color2=="red"))):                #cicle if, conditional where color be red or blue
        return 'Magenta'                                                                                #return 'magenta'

