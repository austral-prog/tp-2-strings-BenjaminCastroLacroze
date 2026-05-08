def casting():

    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_descuento = (precio - descuento)
    precio_total = (precio_descuento * cantidad)

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {precio_total}")


