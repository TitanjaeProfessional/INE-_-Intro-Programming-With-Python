# -*- coding: utf-8 -*-
#Program :  A Game with Functions
#Autor: Garcia De Arcos Jose Angel Eduardo ESCOM Student Licenciado en Ciencias de Datos
#course : Introduction to Programming  with python by Santiago Basulto- INE
#Cretaed on Mon Oct 3 2022

def returnName():
    return 'Angel'


print(returnName())


def sum_of_two_numbers(a,b):
    x=a+b
    return x 

print(sum_of_two_numbers(2,3))
print(sum_of_two_numbers(7,1))


def return_none():
    return None

print(return_none() is None)

print ("guess the pattern1")
def my_function(x):
    x=x*2
    return x

print(my_function(2))
print(my_function(3))
print(my_function(5))
print(my_function(9))

print ("guess the pattern2")
def my_function(x):
    x=x*.5
    return x

print(my_function(9))
print(my_function(10))
print(my_function(1))

print ("guess the pattern3")
def my_function(x):
    x=x*5
    return x

print(my_function(2))
print(my_function(3))
print(my_function(5))
print(my_function(9))

print ("guess the pattern4")
def my_function(x):
    x=x*(-1)
    return x

print(my_function(1))
print(my_function(2))
print(my_function(3))
print(my_function(5))

print ("guess the pattern5")
def my_function(x):
    x=abs(x*2)
    return x

print(my_function(2))
print(my_function(3))
print(my_function(-1))
print(my_function(-3))

print ("guess the pattern6")
def my_function(a_string):
    x=len(a_string)
    return x

print(my_function('python'))
print(my_function('Hello World'))
print(my_function('?'))


print ("guess the pattern7")
def my_function(a,b):
    x=a+b
    return x

print(my_function(2,3))
print(my_function(1,9))
print(my_function(-1,4))

print ("guess the pattern8")
def my_function(a,b):
    x=a*b
    return x

print(my_function(2,3))
print(my_function(4,3))
print(my_function(5,5))




print("invoking function")

print("length of hello world")
def test_length_of_hello_world():
    z =len("hello world")
    return z
print(test_length_of_hello_world())

print("Sum of the first 10 numbers")
def test_sum_of_first_10_numbers():
    sum10num=sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
    return sum10num

print(test_sum_of_first_10_numbers())


print("Function argument exercies")

def multiply_by_two(x):
    x=x*2
    return x

two_times_two = multiply_by_two(2)
three_times_two = multiply_by_two(3)
five_times_two = multiply_by_two(5)

print("2x2 = {}".format(two_times_two))
print("3x2 = {}".format(three_times_two))
print("5x2 = {}".format(five_times_two))


print("increment parameter by one")

def increment_parameter_by_one(numbyone):
    numbyone=numbyone+1
    return numbyone

two=increment_parameter_by_one(1)
fifteen=increment_parameter_by_one(14)
twenty_three=increment_parameter_by_one(22)
print(two)
print(fifteen)
print(twenty_three)    


print("increment parameter by parameter")

def increment_by(numparameter1,numparameter2):
    numincrparameter_sum_parameter=numparameter1+numparameter2
    return numincrparameter_sum_parameter

print(increment_by(1, 4))
print(increment_by(2, 8))


print ("guess the pattern9")
def my_function(a_string):
    b="X_"
    d="_X"
    x=b+(a_string)+d
    return x

print(my_function('python'))
print(my_function('Hello World'))
print(my_function('?'))

print("fix Simple add")

def add(a,b):
    if type(a) != int or type (b)!= int :
        return None
    return a+b


print(add(2,'a'))
print(add(2,3))
    
    
