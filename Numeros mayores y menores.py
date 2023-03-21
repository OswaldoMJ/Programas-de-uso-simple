print("Bienvenido")
Primerval = int(input("Ingrese primer valor \n "))
Segundoval = int(input("Ingrese segundo valor \n "))

if Primerval < Segundoval:
    print(f"El numero mayor es {Segundoval}")
    print(f"El numero menor es {Primerval}")
elif Primerval == Segundoval:
    print(f"Los valores son iguales")
elif Primerval > Segundoval:
    print(f"El numero es mayor {Primerval}" )
    print(f"El numero menor es {Segundoval}")
