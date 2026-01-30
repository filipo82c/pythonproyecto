import gestion_herramientas
import gestion_usuarios
import prestamos
from logs import registrar_evento

registrar_evento("Administrador inicio sesion")
registrar_evento("Administrador cerro sesion")

def admin_menu():
    while True:
        print("\n=== Menu del Administrador ===")
        print("1. Gestion de usuarios")
        print("2. Gestion herramientas")
        print("3. Prestamos pendientes / Historial")
        print("4. Reporte: prestamos activos y vencidos")
        print("5. Reporte: herramientas con stock bajo")
        print("6. Salir")
        opcion =  input("seleccione una opcion: ")
        if opcion == "1":
            gestion_usuarios.usuarios_menu()
        elif opcion == "2":
            gestion_herramientas.herramientas_menu()
        elif opcion == "3":
            prestamos.prestamos_menu(admin=True)
        elif opcion == "4":
            prestamos.prestamos_activos_vencidos()
        elif opcion == "5":
            gestion_herramientas.herramientas_stock_bajo()
        elif opcion == "6":
            print("Sesion de administrador cerrado")
            break
        else:
            print("Opcion invalida. Intente nuevamente")

        
            