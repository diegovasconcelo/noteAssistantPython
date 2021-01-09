import notas.nota as modelo 

class Acciones:

    def crear(self, usuario):
        print(f"\n Ok {usuario[1]} vamos a crear la nota :D")

        titulo=input("Coloca el título de la nota: ")
        descripcion=input("Bien! Ahora la descripción: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Se creó con éxito tu nota: {nota.titulo}")

        else:
            print(f"\n Lo siento {usuario[1]} no se pudo guardar tu nota (-_-) ")

    def mostrar(self,usuario):
        print(f"\n Estas son tus notas {usuario[1]}")

        nota=modelo.Nota(usuario[0])
        notas=nota.listar()

        for nota in notas:
            print("\n /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
            print("\n")
            print(f"titulo: {nota[2]}")
            print(f"Descripción: {nota[3]}")
            print(f"Fecha de creación: {nota[4]}")
            print("\n /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
    
    def borrar(self, usuario):
        print(f"\n Bien {usuario[1]}, vamos a elimnar unas notas!")

        titulo=input("\n Pon el titulo de la nota a eliminar: ")

        nota=modelo.Nota(usuario[0], titulo)
        eliminar=nota.eliminar()

        if eliminar[0] >= 1:
            print(f"\n Eliminé la nota {nota.titulo}")
        else:
            print("\n No pude borrar la nota (o.O), sorry!")


