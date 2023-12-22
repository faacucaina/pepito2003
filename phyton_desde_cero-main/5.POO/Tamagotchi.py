class Tamagotchi:
    def __init__(self):
        self.nombre = str
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True
        self.descripcion = str

    def crear_bicho(self):
        self.nombre = input("Ingrese nombre de si Tamagotchi: ")
        self.descripcion = input("Relice una descripcion de su apariencia: ")
    def mostrar_estado(self):
        print(f"Nivel de Energía: {self.nivel_energia}")
        print(f"Nivel de Hambre: {self.nivel_hambre}")
        print(f"Estado de Humor: {self.humor}")
        print()

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia -= 15
        self.verificar_estado()
        self.actualizar_humor()

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10

        self.verificar_estado()
        self.actualizar_humor()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5

        self.verificar_estado()
        self.actualizar_humor()

    def verificar_estado(self):
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
        if self.nivel_energia <= 0:
            self.esta_vivo = False

    def actualizar_humor(self):
        if self.nivel_felicidad < 20:
            self.humor = "enojado"
        elif 20 <= self.nivel_felicidad < 50:
            self.humor = "triste"
        elif 50 <= self.nivel_felicidad < 80:
            self.humor = "indiferente"
        else:
            self.humor = "feliz"



tamagotchi = Tamagotchi()
tamagotchi.crear_bicho()
tamagotchi.mostrar_estado()

print(f"{tamagotchi.nombre} se esta alimentando")
print (f"{tamagotchi.nombre}:- QUE RICOO!! QUIERO MAS!")
print(f"Estado:")
tamagotchi.alimentar()
tamagotchi.actualizar_humor()
tamagotchi.mostrar_estado()

print(f"{tamagotchi.nombre} esta jugando")
print (f"{tamagotchi.nombre}:- QUE DIVERTIDO!!")
print(f"Estado:")
tamagotchi.jugar()
tamagotchi.actualizar_humor()
tamagotchi.mostrar_estado()

print(f"{tamagotchi.nombre} se encuentra durmiendo")
print (f"{tamagotchi.nombre}:- ZzzZZZZzzzzZZZZz")
print(f"Estado:")
tamagotchi.dormir()
tamagotchi.actualizar_humor()
tamagotchi.mostrar_estado()