#2. Escribe un programa que solicite el nombre, el apellido y la edad del usuario e imprima un saludo y su año de nacimiento. Tomar el año actual como constante (2023)


nombre=input("Dame tu nombre\n")
apellido=input ("Dame tu apellido\n")
edad=int (input ("Dame tu edad\n"))

naci= 2023-edad


print("Hola "+nombre+" "+apellido+" naciste en ",naci)