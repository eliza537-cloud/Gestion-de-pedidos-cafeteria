from enum import Enum

class Persona():
    def __init__(self,idpersona:int,nombre:str,email:str):
        self.idpersona=idpersona
        self.nombre=nombre
        self.correo=email

    def login(self):
        print(f"{self.nombre} a iniciado sesion con el correo {self.correo}")

    def actualizarPerfil(self,nuevo_nombre,nuevo_correo):
        print(f"Haz actualizado tu perfil con el nombre de: {nuevo_nombre} y correo: {nuevo_correo}")


class ProductoBase():
    def __init__(self,idproducto:int,nombre:str,preciobase:float):
        self.idproducto=idproducto
        self.nombreprod=nombre
        self.preciobase=preciobase
    def calcularPrecioFinal(self):
        return self.preciobase


class Temperatura(Enum):
    FRIO="FRIO"
    CALIENTE="CALIENTE"

class Bebida(ProductoBase):
    def __init__(self,idproducto,nombre,preciobase,tamaño:str,temperatura:Temperatura,):
        super().__init__(idproducto,nombre,preciobase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]

    def agregarextra(self,precio_extra,nombre_extra):
        self.modificadores.append(precio_extra)
        print(f"El extra {nombre_extra}, se agrego por el precio de {precio_extra}")

    def calcularPrecioFinal(self):
        total_extras=sum(self.modificadores)
        precio_final=self.preciobase + total_extras
        return precio_final
    
class Postre(ProductoBase):
    def __init__(self, idproducto, nombre, preciobase,esVegano:bool,sinGluten:bool):
        super().__init__(idproducto, nombre, preciobase)
        self.vegan=esVegano
        self.gluten=sinGluten
        

class Rol(Enum):
    BARISTA="BARISTA"
    MESERO="MESERO"
    GERENTE="GERENTE"

class Estado(Enum):
    PENDIENTE="PENDIENTE"
    PREPARADO="PREPARADO"
    ENTREGADO="ENTREGADO"


class Pedido():
    def __init__(self,idpedido:int,estado:Estado,productos):
        self.idpedido=idpedido
        self.estado=estado
        self.productos=productos
        self.total=0
    
    def calcularTotal(self):
        suma_acumulada=0
        for producto in self.productos:
            suma_acumulada+=producto.calcularPrecioFinal()
        self.total=suma_acumulada
        return self.total
    
    def validarStock(self,inventario):
        for producto in self.productos:
            stock=inventario.ingredientes.get(producto.nombreprod,0)
            if stock <= 0:
                print(f"No hay suficiente stock de {producto.nombreprod}")
                inventario.notificarFaltantes()
                return False
            print("Stock válido. Todo los ingredientes están disponibles")
            return True 
        
    def mostrarResumen(self):
        print(f"\n---Resumen del Pedido ID: {self.idpedido}---")
        for productos in self.productos:
            print(f"*{productos.nombreprod}: ${productos.calcularPrecioFinal()}")
        print(f"TOTAL FINAL: ${self.total}")
        print("----------------------------------")
            
    
class Empleado(Persona):
    def __init__(self,idpersona,nombre,email,idempleado:str,rol:Rol):
        super().__init__(idpersona,nombre,email)
        self.idempleado=idempleado
        self.rol=rol
    def actualizarinventario(self,inventario,ingrediente,cantidad):
        if ingrediente in inventario.ingredientes:
            inventario.ingredientes[ingrediente]+=cantidad
            print(f"{self.nombre} ha sido actualizado {inventario.ingredientes[ingrediente]}")
        

    def cambiarestado(self,pedido,nuevo_estado):
        estado_anterior=pedido.estado
        pedido.estado=nuevo_estado
        print(f"Pedido {pedido.idpedido} ha cambiado de {estado_anterior.name} a {nuevo_estado.name}")
        pass

class Inventario():
    def __init__(self,ingredientes=None):
        if ingredientes is None:
            self.ingredientes={
            "Cafe":100,
            "Leche":60,
            "Azúcar":80
            }
        else:
            self.ingredientes=ingredientes
    def reducirStock(self,nombre,cantidad):
        if nombre in self.ingredientes:
            self.ingredientes[nombre]-=cantidad
            print(f"Stock actualizado: {nombre} ahora tiene {self.ingredientes[nombre]}")
        else:
            self.notificarFaltantes()

    def notificarFaltantes(self):
        print("¡Error! El ingrediente no existe en el inventario")



class Cliente(Persona):
    def __init__(self,idperosna,nombre,email,puntos:int):
        super().__init__(idperosna,nombre,email)
        self.puntos=puntos
        self.historialpedidos=[]

    def realizarPedidos(self,lista_productos):
        nuevo_pedido=Pedido(idpedido=1,estado=Estado.PENDIENTE,productos=lista_productos)
        self.historialpedidos.append(nuevo_pedido)
        print("Pedido realizado con éxito")

    def consultarHistorial(self):
        for pedido in self.historialpedidos:
            print(f"Pedido ID:{pedido.idpedido} Estado:{pedido.estado.name}")

    def canjearPuntos(self,pedido_actual):
        puntos_necesarios=30
        descuento=10.0
        if self.puntos>=puntos_necesarios:
            self.puntos-=puntos_necesarios
            pedido_actual.total-=descuento
            print(f"¡Canjeo éxitoso! el descuento aplicado es de ${descuento}")
            print(f"Puntos restantes:{self.puntos}")
            return True
        else:
            print("No tiene suficientes puntos para canjear")
            return False
        



