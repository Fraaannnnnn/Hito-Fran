from visualizar import *
from clase_funciones import *
from registro import *
#Crearemos la funcion de realizar una compra
def realizar_compra(cliente):
    #Aqui crearemos un try para poder controlar mas tarde cualquier tipo de error
    try:
        #Usaremos un if por si el cliente no se encuentra
        if not cliente:
            #Lo mostraremos por pantalla
            print("Cliente no encontrado.")
            return
        #Si el cliente se ha encontrado mostraremos para realizar compras
        print("\nRealizar Compra:")
        #Meteremos en una lista los productos
        productos = []
        #Pediremos al usuario que nos diga el nombre del producto que quiere comprar
        while True:
            nombre_producto = input("Nombre del Producto (dejar en blanco para finalizar): ")
            #Le diremos que si no hay producto que termine con el break
            if not nombre_producto:
                break
            #Le pediremos que nos diga el precio del producto(usaremos un Float para que nos obligue a poner un precio real)
            precio_producto = float(input("Precio del Producto: "))
            #Le diremos que la variable nuevo_producto nos coga el nombre y el precio del producto
            nuevo_producto = Producto(nombre_producto, precio_producto)
            productos.append(nuevo_producto)
        #le diremos que sino nos diga que no se agregaron a la compra
        if not productos:
            print("No se agregaron productos a la compra.")
            return
        #Variable compra sera igual que el cliente comprando el producto
        compra = cliente.realizar_compra(productos)
        #que nos muestre por pantalla que la compra ha sido realizada con exito
        print(f"\nCompra realizada con éxito. Total: ${compra.calcular_total():.2f}\n")
        guardar_compra(cliente)
    #Aqui sera donde controlaremos los errores sea antes, durante o despues de la compra
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error durante la compra: {e}")
#Aqui crearemos el main, que sera donde tendremos las opciones para saber que queremos hacer
def main():
    #El while true donde tendremos las opciones
    while True:
        print("\n1. Registrar Cliente")
        print("2. Visualizar Clientes")
        print("3. Realizar Compra")
        print("4. Salir")
        #Crearemos la variable opciones para que depende del numero que nos de mas tarde coga uno u otro
        opcion = input("Selecciona una opción (1/2/3/4): ")
        #Aqui le diremos que si la variable opciones es igual a un numero nos coga depende del numero una funcion u otra
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            visualizar_clientes()
        elif opcion == '3':
            nombre_cliente = input("Nombre del Cliente para realizar la compra: ")
            cliente_seleccionado = next((c for c in clientes_registrados if c.nombre == nombre_cliente), None)
            realizar_compra(cliente_seleccionado)
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Cargar clientes al iniciar el programa
clientes_registrados = cargar_clientes()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
