import gestion_herramientas
import prestamos

def residente_menu(usuario_id):
    while True:
        print("\n === Menu del Residente ===")
        print("1. Ver Herramientas disponibles")
        print("2. Buscar herramientas")
        print("3. Solicitar un prestamo de herramientas")
        print("4. Ver mi historial de prestamo")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            gestion_herramientas.listar_herramientas()
        elif opcion == "2":
            gestion_herramientas.buscar_herramientas()
        elif opcion == "3":
            prestamos.crear_prestamo(usuario_id)
        elif opcion == "4":
            prestamos.ver_historial(usuario_id)
        elif opcion == "5":
            print("Saliendo del menu de residente")
            break
        else:
            print("Opcion no valida, intentelo de nuevo")
            