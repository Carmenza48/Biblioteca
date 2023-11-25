
import mysql.connector
from tabulate import tabulate


class Libro:

    def _init_(self, titulo, autor, isbn):
        self.id = None
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = True

    def prestar(self, data):
        self.disponibilidad = False
        # Conectamos a la base de datos
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="biblioteca"
        )
        cursor = connection.cursor()

        # Insertamos cada libro en la base de datos
        for libro in self.libros:
            cursor.execute("UPDATE libros SET disponibilidad = (%s) WHERE nombre = (%s)",
                           (self.disponibilidad, data))

        # Guardamos los cambios en la base de datos
        connection.commit()

        # Cerramos la conexión con la base de datos
        connection.close()


class Biblioteca:

    def _init_(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros_disponibles(self):
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="biblioteca"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM libros")
        datos = cursor.fetchall()

        print(tabulate(datos, headers=[
            "ID", "TITULO", "AUTOR", "ISBN", "DISPONIBILIDAD"], tablefmt="pipe"))

    def agregar_libro_de_base_de_datos(self):
        # Conectamos a la base de datos
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="biblioteca"
        )
        cursor = connection.cursor()

        # Insertamos cada libro en la base de datos
        for libro in self.libros:
            cursor.execute("INSERT INTO libros (titulo, autor, isbn, disponibilidad) VALUES (%s, %s, %s, %s)",
                           (libro.titulo, libro.autor, libro.isbn, libro.disponibilidad))

        # Guardamos los cambios en la base de datos
        connection.commit()

        # Cerramos la conexión con la base de datos
        connection.close()

    def eliminar_libro_de_base_de_datos(self, data):
        # Conectamos a la base de datos
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="biblioteca"
        )
        cursor = connection.cursor()

        # Insertamos cada libro en la base de datos
        for libro in self.libros:
            cursor.execute("DELETE FROM libros WHERE id = (%s)",
                           (data))

        # Guardamos los cambios en la base de datos
        connection.commit()

        # Cerramos la conexión con la base de datos
        connection.close()


# Agregamos el libro a la biblioteca
biblioteca = Biblioteca()

while True:
    select = int(input("Ingrese la opción que desea realizar\n1. Agregar un libro a la biblioteca\n2. Eliminar un libro de la biblioteca\n3. Mostrar los libros de la biblioteca\n4. Prestar el libro\n5. Salir del menú\n$ "))
    match select:
        case 1:
            # Creamos un libro
            # Agregamos un libro a la base de datos
            libro = Libro(input("Ingrese el titulo del libro a agregar: "), input(
                "Ingrese el autor del libro a agregar: "), input("Ingrese el ISBN del libro a agregar: "))

            # Agregamos el libro a la biblioteca
            biblioteca = Biblioteca()
            biblioteca.agregar_libro(libro)

            # Agregamos los datos de la base de datos
            biblioteca.agregar_libro_de_base_de_datos()
            print("\n------------------------------------------------\n")
            print(f"El libro {libro.titulo} ha sido agregado\n")
        case 2:
            data = input("Ingrese el id del libro a eliminar: ")

            # Eliminamos los datos de la base de datos
            biblioteca.eliminar_libro_de_base_de_datos(data)

            print("\n------------------------------------------------\n")
            print(f"El libro {libro.id} ha sido eliminado\n")
        case 3:
            # Imprimimos los libros disponibles
            biblioteca.mostrar_libros_disponibles()

            print("\n------------------------------------------------\n")
        case 4:
            # Prestamos los libros disponibles
            libro.prestar(input("Ingrese el libro que desea prestar: "))

            print("\n------------------------------------------------\n")
            print(f"El libro {libro.id} ha sido prestado\n")
        case 5:
            print("Has salido del menú de opciones")
            break
        case _:
            print("Opción incorrectamente seleccionada")