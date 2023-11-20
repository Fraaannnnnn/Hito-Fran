from clase_funciones import *
from main import clientes_registrados
#Aqui crearemos la funcion que nos servira para registrar a los clientes
def registrar_cliente():
    #Mostraremos por pantalla el registro del cliente
    print("Registro de Cliente:")
    #Crearemos un try para poder controlar si hay algun error
    try:
        #Pediremos al usuario sus datos personales y los iremos registrando en variables 
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo electrónico: ")
        pais = input("País: ")

        #Crearemos un If por si no existe alguno d los campos nos muestre un error de que todos los campos son obligatorios
        if not nombre or not direccion or not telefono or not correo or not pais:
            raise ValueError("Todos los campos son obligatorios.")

        #Intenta crear un nuevo cliente
        nuevo_cliente = Cliente(nombre, direccion, telefono, correo, pais)
        clientes_registrados.append(nuevo_cliente)
        guardar_cliente(nuevo_cliente)
        #Mostraremos por pantalla si el registro ha sido exitoso
        print(f"\n¡Cliente {nombre} registrado con éxito!\n")
    #Esto nos servira para controlar los errores que hayan en el programa
    except ValueError as ve:
        print(f"Error: {ve}")
        #Aqui controlaremos el error que haya durante el registro
    except Exception as e:
        print(f"Error durante el registro del cliente: {e}")
