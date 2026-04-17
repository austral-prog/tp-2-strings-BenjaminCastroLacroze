def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float (input("Ingresar un gasto: "))
    dinero = int (input("Dinero recibido: "))

    vuelto = (dinero - gasto)

    pesos = int (vuelto)
    centavos = round((vuelto - pesos) * 100)

    print(f"Ingresar gasto:")
    print(gasto)
    print(f"Dinero recibido")
    print(dinero)
    print("")
    print(f"Vuelto")
    print("")
    print(f"Pesos:")
    print(pesos)
    print(f"Centavos:")
    print(centavos)


