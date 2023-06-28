# 5. Escribe un script que solicite un número y devuelva notifique al usuario si el número es par o impar

numero= int(input("Dame un numero\n"))

if numero%2==0:
    print(numero," es par")
else:
    print(numero," no es par")