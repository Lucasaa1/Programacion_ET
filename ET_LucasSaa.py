
def stock_marca(marca):
    encontrado = False
    for producto, data in productos.items():
        if data[0].lower() == marca.lower():
            precio, cantidad = stock.get(producto, [0, 0])
            print(f"Cantidad de {marca} (Modelo: {producto}) en stock: {cantidad}")
            encontrado = True
    if not encontrado:
        print("\nMarca no encontrada")

def busqueda_precio(p_min, p_max):
    encontrados = []
    for modelo in productos:
        precio, cantidad = stock.get(modelo, [0, 0])
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0] + "--" + modelo
            encontrados.append(marca)
    if not encontrados:
        print("No hay notebookes en ese rango de precios")
    else:
        encontrados.sort()
        print("\nNotebooks entre los precios consultas son: ")
        for item in encontrados:
            print(item)

def eliminar_producto():
    while True:
        modelo = input("Ingrese el código del producto a eliminar: ").strip()
        if modelo in productos:
            del productos[modelo]
            del stock[modelo]
            print(f"\nProducto {modelo} eliminado correctamente.\n")
            repetir = input("Desea eliminar otro producto? (Responda únicamente con un SI o con un NO): ").lower()
            if repetir == "si":
                continue
            else:
                break
        else:
            print("Error. El producto no existe o fue ingresado incorrectamente.")
        

def menu():
    while True:
        print("\n*** Menú Principal ***")
        print("1. Stock Marca")
        print("2. Búsqueda por precio")
        print("3. Eliminar producto")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                marca = input("Ingrese marca a buscar: ").strip()
                stock_marca(marca)
            elif opcion == 2:
                print("Ingrese un rango de precios a buscar:")
                while True:
                    try:
                        p_min = int(input("Ingrese límite inferior del rango de precios: "))
                        p_max = int(input("Ingrese límite superior del rango de precios: "))
                        if p_min < p_max:
                            break
                        else:
                            print("Debe ingresar valores enteros!! (Además, el limite inferior debe ser menor que el limite superior)")
                            continue
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                busqueda_precio(p_min, p_max)
            elif opcion == 3:
                eliminar_producto()
            elif opcion == 4:
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    menu()
