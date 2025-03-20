# Variables
x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))

#Valores
print("###########################")
print("Este es el valor de x: ", x)
print("Este es el valor de y: ", y)
print("###########################")

#Calculadora
suma = x+y
resta = x-y
multiplicacion=x*y
divicion=x/y

print("Ingresa una de las siguientes opciones para calcular suma, resta, multiplicacion o division")
operacion = input("Ingrese la operacion que quiere realizar: ")

if operacion == "suma":
    print("Suma de", x, "+", y, "es igual a: ")
    print(suma)
elif operacion == "resta":
    print("Resta de", x, "-", y, "es igual a: ")
    print(resta)
elif operacion == "multiplicacion":
    print("Multiplicacion de", x,"*",y, "es igual a: ")
    print(multiplicacion)
elif operacion == "division":
    print("Division de", x,"/",y, "es igual a: ")
    print(divicion)

print("Fin del calculo")



