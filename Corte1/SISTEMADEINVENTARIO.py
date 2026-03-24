# --------- SISTEMA DE INVENTARIO ---------

# Tupla (categorías fijas)
categorias = ("Tecnología", "Alimentos", "Ropa", "Hogar")

# Lista donde se guardan los productos
productos = []

# Mensaje de bienvenida
print("=== BIENVENIDO AL SISTEMA DE INVENTARIO ===")

# Función para agregar producto
def agregar_producto():
    print("\n--- Agregar Producto ---")
    
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    
    try:
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
    except:
        print("Error: precio o cantidad inválidos")
        return
    
    # Selección de categoría por número
    print("\nCategorías disponibles:")
    for i, cat in enumerate(categorias, 1):
        print(f"{i}. {cat}")
    
    try:
        opcion_cat = int(input("Seleccione el número de la categoría: "))
        
        if opcion_cat < 1 or opcion_cat > len(categorias):
            print("Número inválido")
            return
        
        categoria = categorias[opcion_cat - 1]
    
    except:
        print("Error: debe ingresar un número")
        return
    
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    
    productos.append(producto)
    print("Producto agregado correctamente")

# Función para mostrar productos
def mostrar_productos():
    print("\n--- Lista de Productos ---")
    
    if len(productos) == 0:
        print("No hay productos registrados")
        return
    
    for p in productos:
        print(p)

# Función para buscar producto
def buscar_producto():
    print("\n--- Buscar Producto ---")
    codigo = input("Ingrese código: ")
    
    for p in productos:
        if p["codigo"] == codigo:
            print("Producto encontrado:", p)
            return
    
    print("Producto no encontrado")

# Función para eliminar producto
def eliminar_producto():
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese código: ")
    
    for p in productos:
        if p["codigo"] == codigo:
            productos.remove(p)
            print("Producto eliminado")
            return
    
    print("Producto no encontrado")

# Menú principal
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
