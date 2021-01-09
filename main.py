"""
Proyecto Python y MySQL:
    -Abrir asistente
    -Login o registro
    -Si elegimos regirstro, creará un usuario nuevo en la BD
    -Se elegimos login, identificará al usuario y preguntará si:
    -Crear nota, mostrar notas, borrarlas.
"""
from usuarios import acciones

print("""
HOLA! SOY TU ASISTENTE DE NOTAS :D, COMENCEMOS! \n
    • Registro
    • Login
""")

hazEl=acciones.Acciones() 

accion=input("Que deseas hacer? ")

if accion == "Registro" or accion == "registro":
    hazEl.registro()

elif accion == "Login" or accion =="login":
    hazEl.login()