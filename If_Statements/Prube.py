# -*- coding: utf-8 -*-
#Program :  Prueba
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Created on Mon Oct 6  2022

#divisible_by_11 = 11
#is_583_divisible_by_11 = None
#is_911_divisible_by_11 = None

#number_583 = 583

#if number_583 % divisible_by_11 == 0:
 #   is_583_divisible_by_11 = True
#else:
 #   is_583_divisible_by_11 = False


#is_911_divisible_by_11 = None
#number_911 = 911

#if number_911 % divisible_by_11 == 0:
 #   is_911_divisible_by_11 = True
#else:
#    is_911_divisible_by_11 = False
    
#print(is_583_divisible_by_11)
#print(is_911_divisible_by_11)


def greatest_parameter(a, b, c, d, e):
    greatest = a

    if b > a:
        greatest = b
        print(greatest)

    if c > greatest:
        greatest = c
        print(greatest)

    if d > greatest:
        greatest = d
        print(greatest)

    if e > greatest:
        greatest = e
        print(greatest)

    return  greatest

greatest_parameter(2, 4, 9, 1, 1)


def fr(a,b,c,d,e):
    listaval = (a,b,c,d,e)
    gp=a
    for i in range(5):
        if(gp<listaval[i]):
            gp=listaval[i]
    print(gp)
    return gp

fr(1,2,3,4,5)