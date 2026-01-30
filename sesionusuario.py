from admin_menu import admin_menu
from residente_menu import residente_menu
from gestion_usuarios import cargar_usuarios, crear_usuario
usuarios = cargar_usuarios()
admins = [u for u in usuarios if u["tipo_usuario"].lower() == "administrador"]
if not admins:
    print("No existe ningun administrador en el sistema")
    print("Debe crear el primer administrador")
    crear_usuario("administrador")
print("Seleccione su tipo de usuario:")
print("1: Administrador")
print("2: Residente")
print("3: Salir")
opcion = input("Seleccione una opcion (1 , 2 o 3): ")
if opcion == "1" or opcion == "2":
    usuarios = cargar_usuarios()
    usuario_ingresado = input("Usuario: ").strip()
    contraseña_ingresada = input("Contraseña: ").strip()
    encontrado = False
    for u in usuarios:
        if u["usuario"].lower() == usuario_ingresado.lower() and u["contraseña"] == contraseña_ingresada:
            encontrado = True
            print("Inicio de sesion exitoso")
            if u["tipo_usuario"].lower() == "administrador":
                admin_menu()
            elif u["tipo_usuario"].lower() == "residente":
                residente_menu(usuario_id=u["id"])
            break
    if not encontrado:
        print("Usuario o contraseña incorrectos")
elif opcion == "3":
    print("Saliendo del programa")
    exit()
else:
    print("Opcion no valida")
    
    