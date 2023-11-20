#Esta es la defincon de la clase producto
class Producto:
    #La clase Producto tiene dos atributos: nombre y precio
    #El método __init__ es el constructor de la clase, que inicializa los atributos cuando se crea una instancia.
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#Esta es la funcion de enviar sms 
def enviar_sms(numero_telefono, mensaje):
    #Mostraremos por pantalla sms enviado al numero que tengamos del cliente con algun mensaje
    print(f"SMS enviado al número {numero_telefono}: {mensaje}")

##Esta es la defincon de la clase cliente
class Cliente:
    #La clase Cliente tiene atributos como nombre, dirección, teléfono, correo y país.
    def __init__(self, nombre, direccion, telefono, correo, pais):
        #self se utiliza para referirse a la instancia recién creada de la clase
        #En este caso los utilizaremos con los datos de registro del cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.pais = pais
        self.compras = []
    #Aqui crearemos la funcion de realizar compra que sera para que se realice la compra sin problema
    def realizar_compra(nombre, productos):
        #Aqui sera la variable de nueva compra
        nueva_compra = Compra(productos)
        nombre.compras.append(nueva_compra)
        return nueva_compra

class Compra:
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

# Archivos para almacenar los clientes y las compras
archivo_clientes = "clientes.txt"
archivo_compras_formato = "compras_{}.txt"  # El {} se remplazará con el nombre del cliente

def cargar_clientes():
    try:
        with open(archivo_clientes, 'r') as archivo:
            lineas = archivo.readlines()
        clientes = [Cliente(*linea.strip().split(',')) for linea in lineas]
        return clientes
    except FileNotFoundError:
        return []

def guardar_cliente(cliente):
    with open(archivo_clientes, 'a') as archivo:
        archivo.write(f"{cliente.nombre},{cliente.direccion},{cliente.telefono},{cliente.correo},{cliente.pais}\n")

def guardar_compra(cliente):
    archivo_compras = archivo_compras_formato.format(cliente.nombre)
    with open(archivo_compras, 'a') as archivo:
        for compra in cliente.compras:
            productos = ",".join(f"{producto.nombre}:{producto.precio}" for producto in compra.productos)
            archivo.write(f"{productos}\n")
