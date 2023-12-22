
class Cuenta():
    def __init__(self,nombre,apellido,contraseña, saldo = 0 ):
        nombre = str(nombre)
        apellido = str(apellido)
        contraseña = str(contraseña)
        self.saldo = saldo
    def crearCuenta(self):
        print(f"CREAR CUENTA DE CAJERO")
        print(f"        ")
        self.nombre = str(input("Ingrese Nombre: "))
        print(f"------------------------------")
        self.apellido = str(input("Ingrese Apellido: "))
        print(f"------------------------------")
        self.contraseña = str(input("Ingrese una Contraseña: "))
        print(f"------------------------------")
        print(f"   CUENTA CREADA CON EXITO   ")
        print(f"==============================")
cuenta = Cuenta(" ", " " ," ", )
cuenta.crearCuenta()

cuenta1 = Cuenta("Facundo", "Perez", "aaa", 300)


class Cajero():

    def __init__(self, cuenta, cuenta1):
        cuenta = cuenta
        cuenta1 = cuenta1

    def menu(self):
        while cuenta.saldo == 0:
            print(f"____________________________________")
            print(f"DEBE INGRESAR DINERO ANTES DE OPERAR")
            print(f"                                    ")
            self.ingresar()
        print(f"--------------------------")
        print(f"Operaciones.")
        print(f"        1. Ingresar dinero.")
        print(f"        2. Retirar dinero.")
        print(f"        3. Transferir dinero.")
        print(f"        4. Consultar cuenta.")
        print(f"        5. Salir")

    def ingresar(self):
        ingreso= int(input("Ingrese el monto que desea ingresar: "))
        cuenta.saldo += ingreso
        print(f"----INGRESO EXITOSO----")
        

    def retirar(self):
        
        retiro = int(input("Ingrese el monto que desea retirar: "))
        if cuenta.saldo >= retiro:
            cuenta.saldo -= retiro
            print(f"----RETIRO EXITOSO----")
        else:
            print("Saldo insuficiente. Operación no permitida.")
        
        

    def consultar(self):
        print(f"_____________________________________")
        print(f"Su saldo en cuenta es ${cuenta.saldo}")
        print(f"_____________________________________")
        
    def tranferencia(self):
        traferecia = int(input("Ingrese el monto que desea transferir: "))
        if traferecia <= cuenta.saldo:
            cuenta.saldo -= traferecia
            cuenta1.saldo += traferecia  
            print(f"----TRANSFERENCIA EXITOSA----")
            print(f"--Saldo de otra cuenta: ${cuenta1.saldo}--")
            
        else:
            print(f"_____________________________")
            print(f"Saldo insuficiente.")
        
        

    def run(self):
        


        intentos = 3
        
        for intento in range(1, intentos + 1):
            
                contraseña = input("INGRESE CONTRASEÑA DE INICIO: ")
                if contraseña == cuenta.contraseña:
                    print("Contraseña correcta. ")
                    break  
                else:
                    print("Contraseña incorrecta.")

                if intento == intentos:
                    print("Número máximo de intentos")
                    return 
        while True:
                    self.menu()
                    seleccion = int(input("Selecciona una opción: "))     
                    if seleccion <= 5:

                        if seleccion == 1:
                            self.ingresar()
                    
                        elif seleccion == 2:
                    
                            self.retirar()
                    
                        elif seleccion == 3:
                            self.tranferencia()
                    
                        elif seleccion == 4:
                            self.consultar()
                
                        elif seleccion == 5:
                            print("Saliendo de la cuenta")
                            break
                    else:
                        print("----Opcion invalida, elija opcion del 1 al 5----")


cajero = Cajero(cuenta,cuenta1)
cajero.run()








