import usuarios.usuario as modelo
import notas.acciones 

class Acciones:

    def registro(self):
        print ("\n Ok! Te registraré :)")

        nombre=input("\n Introduce tu nombre: ")
        apellidos=input("\n Introduce tu apellido: ")
        email=input("\n Introduce tu email: ")
        password=input("\n Introduce tu contraseña: ")

        usuario=modelo.Usuario(nombre,apellidos,email,password)
        registro=usuario.registrar()

        if registro[0] >= 1:
            print(f"\n Okey {registro[1].nombre} te registraste con el email {registro[1].email}")
        else:
            print ("Ups! Algo salió mal :( ")
    
    def login(self):
        print ("Ok! Identificate :)")

        try:
            email=input("\n Introduce tu email: ")
            password=input("\n Introduce tu contraseña: ")

            usuario=modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email==login[3]:
                print(f"\n Bienvenido/a {login[1]}, te registraste el día {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print (type(e))
            #print (type(e).__name__)
            print (f"Login incorrecto! :O ")

    def proximasAcciones(self, usuario):
        print("""
        
        Menu principal

        • Crear nota (c)
        • Ver mis notas (v)
        • Eliminar nota (e)
        • Salir (s)
        """)

        accion = input("¿ Qué quieres hacer o_O ?: ")
        hazEl=notas.acciones.Acciones()

        if accion == "C" or accion == "c":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        if accion == "V" or accion == "v":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        if accion == "E" or accion == "e":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "S" or accion == "s":
            print(f"Bye! Vuelve pronto {usuario[1]} :) ")
            exit()
