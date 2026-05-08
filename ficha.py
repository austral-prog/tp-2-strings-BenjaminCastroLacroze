def ficha():

    nombre = input().strip().title()
    email = input().lower().strip()

    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {nombre}")
    print(f"Email: {email}")

    print(f"Caracteres en nombre: {len(nombre)}")

    espacio_nombre = nombre.find(" ")
    iniciales_nombre = nombre[0] + nombre[espacio_nombre + 1]
    print(f"Iniciales: {iniciales_nombre}")

    usuario = (nombre[espacio_nombre + 1:] + "." + nombre[: espacio_nombre]).lower()
    print(f"Usuario: {usuario}")

    print(f"Email valido: {'@' in email}")
    
    arroba_email = email.find("@")
    dominio_email = email[arroba_email + 1:]
    print(f"Dominio: {dominio_email}")

    print (f"Nombre para archivo: {(nombre.replace( ' ', '_'))}")
    print(f"Cantidad de a: {(nombre.count('a'))}")

    print(f"Codigo secreto: {(nombre[::-1]).upper()}")

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    suma = nota1 + nota2 + nota3
    promedio = (nota1 + nota2 + nota3) / 3

    print(f"Suma: {suma}")
    print(f"Promedio: {float(promedio)}")
    print (f"Promedio entero: {int(promedio)}")

    print("=" * 24)


