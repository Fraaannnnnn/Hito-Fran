#necesitaremos insertar "clases_funciones" para que pueda coger funciones de ese mismo apartado
from clase_funciones import *

#crearemos la funcion de visualizar clientes para ver los clientes que hay registrados
def visualizar_clientes():
    #Imprimiremos por pantalla los clientes registrados
    print("\nClientes Registrados:")
    #Crearemos un Try para que se cree como una caja en la cual si hay un error lo podamos captar en el Except
    try:
        clientes = cargar_clientes()
        #Utilizaremos un If para ver si no hay clientes registrados
        if not clientes:
            print("No hay clientes registrados.")
        #Y aqui sera por si existe el cliente que nos lo muestrepor pantalla
        else:
            for i, cliente in enumerate(clientes, 1):
                print(f"{i}. Nombre: {cliente.nombre}, Teléfono: {cliente.telefono}, Correo: {cliente.correo}")

        print("\n")
    #Aqui captaremos el error en un caso que haya error para visualizar cual es el error
    except Exception as e:
        print(f"Error al visualizar clientes: {e}")
