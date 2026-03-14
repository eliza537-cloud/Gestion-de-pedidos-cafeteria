from cafeteria import*
def main():
    stock_inicial={"Cafe":100,"Leche":50,"Azucar":80}
    mi_inventario=Inventario(stock_inicial)
    #se crea los productos y el personal
    capuchino=Bebida(1,"Capuchino",25,"Grande",Temperatura.CALIENTE)
    capuchino.agregarextra(10,"Leche de almendra")
    cafe_americano=Bebida(3,"Café Americano",45,"Mediano",Temperatura.FRIO)
    chocolate=Bebida(4,"Chcolate",50,"Grande",Temperatura.CALIENTE)
    soda=Bebida(5,"Soda italiana",50,"Grande",Temperatura.FRIO)


    pastel=Postre(5,"Pastel de chocolate",15,False,True)
    pay=Postre(6,"Pay de queso",35,False,False)
    Roles=Postre(7,"Rol de canela",25,True,False)
    Galletas=Postre(8,"Galleta de chocolate",35,True,True)

    usuario1=Cliente(1,"Raquel","raquel.gr.7@gmail.com",puntos=100)
    usuario2=Cliente(2,"Alejandro","ale@gmail.com",puntos=90)
    usuario3=Cliente(3,"Daniel","daniel@gamil.com",puntos=10)
    usuario4=Cliente(4,"Rafael","rafa@gmail.com",puntos=60)
    usuario5=Cliente(5,"Adriana","adri@gmail.com",puntos=80)

    barista=Empleado("1","Laura","lau@gmail.com","E-1",Rol.BARISTA)
    gerente=Empleado("2","Raul","rau@gmail.com","E-2",Rol.GERENTE)



    #Pedido del cliente
    print("----Iniciando Pedido----")
    usuario1.login()
    lista_productos=[capuchino,pastel]
    usuario1.realizarPedidos(lista_productos)
    pedido_actual=usuario1.historialpedidos[-1]

    #Se valida stock
    total=pedido_actual.calcularTotal()
    print(f"Total del pedido: ${total}")
   

    #canjear puntos
    usuario1.canjearPuntos(pedido_actual)

    #Cambiar estado (por el empleado)
    barista.cambiarestado(pedido_actual,Estado.PREPARADO)
    barista.cambiarestado(pedido_actual,Estado.ENTREGADO)

    #Ver historial
    print("\n ----Historial del cliente----")
    usuario1.consultarHistorial()
    
    pedido_actual.mostrarResumen()


#pedido2
    print("----Iniciando Pedido----")
    usuario2.login()
    lista_productos=[chocolate,Roles]
    usuario2.realizarPedidos(lista_productos)
    pedido_actual=usuario2.historialpedidos[-1]

    #Se valida stock
    total=pedido_actual.calcularTotal()
    print(f"Total del pedido: ${total}")
   

    #canjear puntos
    usuario2.canjearPuntos(pedido_actual)

    #Cambiar estado (por el empleado)
    barista.cambiarestado(pedido_actual,Estado.PREPARADO)
    barista.cambiarestado(pedido_actual,Estado.ENTREGADO)

    #Ver historial
    print("\n ----Historial del cliente----")
    usuario2.consultarHistorial()
    
    pedido_actual.mostrarResumen()

#pedido3

    print("----Iniciando Pedido----")
    usuario3.login()
    lista_productos=[capuchino,pay]
    usuario3.realizarPedidos(lista_productos)
    pedido_actual=usuario3.historialpedidos[-1]

    #Se valida stock
    total=pedido_actual.calcularTotal()
    print(f"Total del pedido: ${total}")
   

    #canjear puntos
    usuario3.canjearPuntos(pedido_actual)

    #Cambiar estado (por el empleado)
    barista.cambiarestado(pedido_actual,Estado.PREPARADO)
    barista.cambiarestado(pedido_actual,Estado.ENTREGADO)

    #Ver historial
    print("\n ----Historial del cliente----")
    usuario3.consultarHistorial()
    
    pedido_actual.mostrarResumen()

#pedido4

    print("----Iniciando Pedido----")
    usuario4.login()
    lista_productos=[cafe_americano,Galletas]
    usuario4.realizarPedidos(lista_productos)
    pedido_actual=usuario4.historialpedidos[-1]

    #Se valida stock
    total=pedido_actual.calcularTotal()
    print(f"Total del pedido: ${total}")
   

    #canjear puntos
    usuario4.canjearPuntos(pedido_actual)

    #Cambiar estado (por el empleado)
    barista.cambiarestado(pedido_actual,Estado.PREPARADO)
    barista.cambiarestado(pedido_actual,Estado.ENTREGADO)

    #Ver historial
    print("\n ----Historial del cliente----")
    usuario4.consultarHistorial()
    
    pedido_actual.mostrarResumen()

#pedido5
    print("----Iniciando Pedido----")
    usuario5.login()
    lista_productos=[soda,pay]
    usuario5.realizarPedidos(lista_productos)
    pedido_actual=usuario5.historialpedidos[-1]

    #Se valida stock
    total=pedido_actual.calcularTotal()
    print(f"Total del pedido: ${total}")
   

    #canjear puntos
    usuario5.canjearPuntos(pedido_actual)

    #Cambiar estado (por el empleado)
    barista.cambiarestado(pedido_actual,Estado.PREPARADO)
    barista.cambiarestado(pedido_actual,Estado.ENTREGADO)

    #Ver historial
    print("\n ----Historial del cliente----")
    usuario5.consultarHistorial()
    
    pedido_actual.mostrarResumen()

if __name__=="__main__":
    main()
       

    
