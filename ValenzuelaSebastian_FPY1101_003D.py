productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']

}

stock = {'8475HD': [387990,10],
        '2175HD': [327990,4],
        'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], 
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0]
}

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            total += stock.get(modelo, [0, 0])[1]
    print(f"Stock total de {marca.capitalize()}: {total}")

def busqueda_precio(p_min, p_max):
    try:
        p_min = int(p_min)
        p_max = int(p_max)
    except ValueError:
        print("Debe ingresar valores enteros!!")
        return
    
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}-----{modelo}")

    if resultados:
        for item in sorted(resultados):
            print(item)
    else:
        print("No hay noteboock en ese rango de precio.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
    
def main():
    while True: 
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir")
        opcion = input("Ingrese opción: ")

        if opcion == "4":
            print("\nPrograma finalizado.")
            break
        elif opcion == "1":
            marca = input("\nIngrese marca a consultar: ")
            stock_marca(marca)
        elif opcion == "2":
            p_min = input("Ingrese precio minimo: ")
            p_max = input("Ingrese precio maximo: ")
            busqueda_precio(p_min, p_max)
        elif opcion == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    p = int(input("Ingrese precio nuevo: "))
                    if p <= 0:
                        print("El precio debe tener un valor mayor a cero!!")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero para el precio!!")
                    continue

                if actualizar_precio(modelo, p):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                
                repetir = input("¿Desea actualizar otro precio? (s/n)").lower()
                if repetir != "si":
                    break
        else:
            print("Debe seleccionar una opcion valida!!")

main()

