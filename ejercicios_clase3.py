#Haz un programa en el cual primero compruebe que a = 11  y luego compruebe que b = 12 y saque ambos por pantalla
a = 11
b = 12

if(a == 11):
    print("a es igual a :", a)
if(b == 12):
    print("b es igual a :", b)



#Haz un programa que compruebe si lo que ha introducido el usuario es un número par o impar

numero = int(input("Introduce un número: "))

if(numero % 2 == 0):
    print("Es par")
else:
    print("Es impar")

#Crea dos variables numéricas y réstalas, acto seguido haz que se muestre el resutlado por pantalla
a = 2
b = 3

print(b - a)


#Crea dos variables numéricas y multiplícalas, acto seguido haz que se muestre el resutlado por pantalla

print(a * b)

#Muestra con while los números del 1 al 75, y al acabar un mensaje de finalización

i = 0
while i < 76:
    print(i)
    i = i + 1
print("Fin")

#Muestra con for los números del 1 al 51

for x in range(1, 51, 1):
    print(x)

#Haz un programa que compruebe el número de dígitos (máximo cuatro) que tiene un número que le introduce el usuario (doble condicional: if x< and x>)

digitos = int(input("Introduce un número de 1 a 4 dígitos: "))
contador = len(str(digitos))

def cuenta_digitos():
    if(contador < 4):
        print("El número introducido tiene más de 4 dígitos.")
    elif:
        print("El número introducido tiene menos de 1 dígito.")
    else:
        print("El número introducido es el ", digitos)
cuenta_digitos()


#Ahora escribe un programa que compruebe el número de cuatro dígitos más pequeño, y en caso de introducirlo el usuario, lo diga por pantalla.



#Crea un programa en el que pida una variable que necesite diferentes condiciones en base a si es positivo, negativo, o cero y las indique por pantalla en caso de que se cumplan
#(El usuario debe introducir un número)



#De dos números en dos variables (a y b), mostrar por pantalla la que sea mayor (if) con el mensaje: "a es mayor que" y/o "b es mayor que"



#Utiliza la función print() para mostrar por pantalla una división entre números flotantes.



#Haz una multiplicación de 5 carácteres vacíos y sácalos con print() + un string que ponga "5 espacios"



#Crea un programa que compruebe si un número es divisible entre 5 y nos lo diga por pantalla, tanto si lo es como si no.



