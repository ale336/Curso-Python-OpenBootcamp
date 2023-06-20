# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

# año = 2020;

# def es_bisiesto(año):
# 	return not año % 4 and (año % 100 or not año % 400)

# año = 2022

# print("Es bisiesto" if not año % 4 and (año % 100 or  not año % 400) else "No es bisiesto")

def bisiesto(año):
    if not año % 4 and (año % 100 or not año % 400):
        print("Es Bisiesto")
    else:
        print("No Es Bisiesto")
        
año = int(input('Escribe un año : '))

bisiesto(año)