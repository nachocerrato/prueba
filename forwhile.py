for x in range(0, 12, 2):
    print(x)

for x in range(6):
  print(x)
else:
  print("Fin")

nombre = ['Gerard', 'Sebastián', 'Jan', 'Josep']
for x in nombre:
    print(nombre)

for x in nombre:
    print(x)

lista = [1,2,3,4,5,6,7,8,9,10]
for x in lista:
    print (x)

cadena1 = str(input())
cadena2 = cadena1[::-1]
if (cadena1) == (cadena2):
    print("1")
else:
    print("2")


i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break 
  i += 1

for number in range(-3,100):
    if (number % 2 == 0):
        print(number)

n= int(input())
while n>0:
  n-=1
  print(n)

n = 0
while n < 100:
    if (n % 2 == 0):
        print(n)
    n=n+1

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i no es mayor que 6")

names = ['Gerard', 'Jan', 'Josep', 'Rigoberto']
print(enumerate(names))

contador = 0
while contador < 3:
    print("Dentro")
    contador = contador + 1
else:
    print("Inside else")

a = 5
b = 10
if a == 5:
    print("a vale",a)
if b == 10:
    print("b vale",b)

nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")

c = 0
while c <= 5:
    print("c vale", c)
    c+=1

i=1
while(i<=50):
    print(i)
    i += 1   
print('Fin')


for i in range (0,51):
    print(i)


for i in "PythonFinance":
    print(i)


a = 3
b = 7
if (a>b):
    print("a es mayor que b")
else:
    print("b es mayor que a")


cadena1 = str(input("Dame una cadena: "))
cadena_al_reves = cadena1[::-1]

if (cadena1 == cadena_al_reves):
    print("Es un palíndromo")
else:
    print("No lo es")
