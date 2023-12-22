class Carrito():
    def __init__(self):

        self.productos = []
        self.precios = {
            'leche': 50,
            'galletas': 35,
            'gaseosa': 87,
            'huevos': 66,
            'aceite': 110,
            'pan': 20
        }
    def menu(self):
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ver lista de compras")
        print("4. Finalizar compra")
        print("5. Salir")
    

    def agregar(self, producto, cantidad = 1):
        if producto in self.precios:
            self.productos.append({'producto': producto, 'cantidad': cantidad, 'precio': self.precios[producto]} )
        print(f"{cantidad} {producto} añadidos al carrito.")


    def eliminar(self, producto, cantidad):
        if producto in self.precios:
            if producto['producto'] == producto:
                producto['cantidad'] -= cantidad    
            if producto['cantidad'] <=0:
                self.productos.remove(producto)
        print(f"{cantidad} {producto} eliminados del carrito.")
        return


    def ver(self):
        print(f"Los productos en el carrito son: {self.productos}")



    def finalizar(self):
        total = 0
        for producto in self.productos:
            total = (producto['cantidad'] * self.precios[producto['producto']])
            
        print(f"El total a pagar es: ${total} ")

    def salir() :
        print("Saliendo del carrito.")
    
    def run(self):

        while True:
            print(f"CARRITO DE COMPRA")
            self.menu()
            seleccion = input("Selecciona una opción: ")

            if seleccion == "1":
                producto = input("Ingrese producto que se va a añadir: ")
                cantidad = int(input("Ingrese la cantidad: "))
                self.agregar(producto, cantidad)
            elif seleccion == "2":
                producto = input("Ingrese producto a eliminar: ")
                cantidad = int(input("Ingrese la cantidad a eliminar: "))
                self.eliminar(producto, cantidad)
            elif seleccion == "3":
                self.ver()
            elif seleccion == "4":
                self.finalizar()
            elif seleccion == "5":
                print(f"SALIENDO DEL CARRITO DE COMPRA")
                self.salir()
            elif seleccion >= "6":
                print("OPCION INVALIDA")

carrito = Carrito()
carrito.run()