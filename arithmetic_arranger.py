print("Bienvenido")
num_1=-1
num_2=-1

# Creación de variables. Se pide al usuario que introduzca los valores de los dos números.
while num_1 == -1:
    num_1=input("Ingrese el primer número: ")
    print(type(num_1))
    num_2=input("Ingrese el segundo número: ")
    print(type(num_2))

# Convierto ambos números en un valor numérico, y pruebo si el usuario introdujo un valor coherente
    try:
        num_1=int(num_1)
        num_2=int(num_2)
    except:
        num_1 = -1
        print("Input inválido, introducir números en ambos campos")

# Se muestran los número para mostrar lo que colocó el usuario.
print("El primer número es ", num_1)
print("El segundo número es ", num_2)

# Acá se decide si se mostrará el resultado de la suma o no.
mostrar = "NONE"
resultado = "NONE"
while resultado == "NONE":
    mostrar=input("¿Quiere que se muestre el resultado o no? (S/N): ")
    if mostrar == "S":
            resultado = "TRUE"
    elif mostrar == "N":
        resultado = "FALSE"
    else:
         print("Opción incorrecta, responda S o N")

# Acá se imprime la cuenta y el resultado en caso de que corresponda.
if resultado == "TRUE":
    print("   ", num_1)
    print("+ ", num_2)
    print("-----")
    print("  ", num_1+num_2)
    print("El resultado es: ", num_1+num_2)
else:
    print("   ", num_1)
    print("+ ", num_2)
    print("-----")