from admin_menu import admin_menu
from residente_menu import residente_menu
print("Seleccione su tipo de usuario:")
print("1: Administrador")
print("2: Residente")
print("3: Salir")
opcion = input("Seleccione una opcion (1 , 2 o 3): ")
if opcion =="1":
    print("Ha seleccionado Administrador")
    usuario1 = "Administrador"
    contraseña1 = "admin123"
    usuario1_ = input("Usuario: ")
    contraseña1_ = input("Contraseña: ") 
    if usuario1 == usuario1_ and contraseña1 == contraseña1_:
        print("Inicio de sesion exitoso (Administrador)")
        admin_menu()
    else:
        print("Usuario o contraseña incorrectos")  
elif opcion == "2":
    print("Ha seleccionado Residente")       
    usuario2 = "Residente"
    contraseña2 = "residente123"   
    usuario2_ = input("Usuario:")
    contraseña2_ = input("Contraseña: ")    
    if usuario2 == usuario2_ and contraseña2 == contraseña2_:
        print("Inicio de sesion exitoso (Residente)")
        residente_menu(usuario_id=1)
    else:
        print("Usuario o contraseña incorrectos")    
elif opcion == "3":
    print("Saliendo del programa")
    exit()   
else:
    print("Opcion no valida ") 