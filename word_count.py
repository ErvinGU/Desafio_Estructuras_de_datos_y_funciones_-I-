import sys


if len(sys.argv) != 2:
    print("<archivo_texto>")
    sys.exit(1)

nombre_archivo = sys.argv[1]

try:
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        texto = file.read()
    
 
    caracteres_distintos = set(texto)
    num_caracteres_distintos = len(caracteres_distintos)
    
    palabras = texto.split()
    palabras_distintas = set(palabras)  
    num_palabras_distintas = len(palabras_distintas)

    
    print(f"El número de caracteres distintos es: {num_caracteres_distintos}")
    print(f"El número de palabras distintas es: {num_palabras_distintas}")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
