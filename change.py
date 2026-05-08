def change():

    gasto = float (input())
    dinero = int (input())

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


