def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Nombre: ").strip().title()
    email = input("Email: ").lower().strip()

    nota1 = int(input("Ingresar primera nota: "))
    nota2 = int(input("Ingresar segunda nota: "))
    nota3 = int(input("Ingresar tercera nota: "))

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


