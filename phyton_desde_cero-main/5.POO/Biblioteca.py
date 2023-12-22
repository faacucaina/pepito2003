class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = int(año)
        self.disponible = True

    def mostrar_datos(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Disponible: {self.disponible}")

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)

    def mostrar_libros(self):
        for libro_actual in self.lista_libros:
            libro_actual.mostrar_datos()

    def prestar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                print(f"Libro '{titulo}' prestado con éxito.")
                return
        print(f"El libro '{titulo}' no está disponible para préstamo.")

    def devolver_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                print(f"Libro '{titulo}' devuelto con éxito.")
                return
        print(f"El libro '{titulo}' no se puede devolver o no pertenece a esta biblioteca.")

    def menu(self):
        while True:
            print("\n----- Menú de la Biblioteca -----")
            print("1. Mostrar libros disponibles")
            print("2. Prestar libro")
            print("3. Devolver libro")
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.mostrar_libros()
            elif opcion == '2':
                titulo = input("Ingrese el título del libro que desea prestar: ")
                self.prestar_libro(titulo)
            elif opcion == '3':
                titulo = input("Ingrese el título del libro que desea devolver: ")
                self.devolver_libro(titulo)
            elif opcion == '4':
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")


libro1 = Libro("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
libro2 = Libro("Foundation", "Isaac Asimov", 1951)
libro3 = Libro("1984", "George Orwell", 1949) 
libro4 = Libro("Ender's Game", "Orson Scott Card", 1985)
libro5 = Libro("Dune", "Frank Herbert", 1965)
biblioteca = Biblioteca()


biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

biblioteca.menu()