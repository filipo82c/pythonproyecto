import json
import os
import controlador as c
Archivo = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(Archivo):
        with open(Archivo, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(Archivo, "r", encoding="utf-8") as f:
        return json.load(f)     
       
def guardar_usuarios(usuarios):
    with open(Archivo, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)  
        
def crear_usuario(tipo_forzado=None):
    usuarios = cargar_usuarios()

    nombres = c.solotexto("Ingrese Nombres: ")
    apellidos = c.solotexto("Ingrese Apellidos: ")
    telefono = c.solonumeros("Telefono: ")
    direccion = input("Direccion: ")

    if tipo_forzado is None:
        while True:
            tipo = input("Tipo de usuario (Administrador/Residente): ").strip().lower()
            if tipo == "administrador" or tipo == "residente":
                break
            print("Debe escribir Administrador o Residente")
    else:
        tipo = tipo_forzado.lower()
        print("Tipo de usuario: Administrador")
    cantidad_tipo = sum(1 for u in usuarios if u["tipo_usuario"].lower() == tipo)
    usuario = f"{tipo} {cantidad_tipo + 1}"

    while True:
        contraseña = input("Contraseña: ").strip()
        if contraseña == "":
            print("La contraseña no puede estar vacia")
        else:
            break
    nuevo = {
        "id": len(usuarios) + 1,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo_usuario": tipo.capitalize(),
        "usuario": usuario,
        "contraseña": contraseña
    }
    usuarios.append(nuevo)
    guardar_usuarios(usuarios)
    print("Usuario creado correctamente")
    print(f"Usuario asignado: {usuario}")
    input("Presione enter para volver al menu")
                
    
def listar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados")
        return
    print("\n--- Lista de Usuarios ---")
    for u in usuarios:
        print(f"{u['id']} - {u['nombres']} {u['apellidos']} {u['direccion']} {u['usuario']} ({u['tipo_usuario']})")  

def buscar_usuario():
    usuarios = cargar_usuarios()
    try:
        id_buscar = int(input("ID del usuario: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    for u in usuarios:
        if u["id"] == id_buscar:
            print("\nUsuario encontrado:")
            print(u)
            return   
    print("usuario no encontrado")

def actualizar_usuario():
    usuarios = cargar_usuarios()
    try:
        id_buscar = int(input("ID del usuario actualizado: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    for u in usuarios:
        if u["id"] == id_buscar:
            u["telefono"] = input("nuevo telefono: ")
            u["direccion"] = input("nueva direccion: ")
            guardar_usuarios(usuarios)
            print("usuario actualizado")
            return
    print("usuario no encontrado")
    
def eliminar_usuario():
    usuarios = cargar_usuarios()
    try:
        id_eliminar = int(input("ID a eliminar: ")) 
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    usuarios = [u for u in usuarios if u["id"] != id_eliminar]
    guardar_usuarios(usuarios)
    print("usuario eliminado")
    
def usuarios_menu():
    while True:
        print("\n--- Gestion de Usuarios ---")
        print("1. Crear Usuario")
        print("2. Listar Usuarios")
        print("3. Buscar Usuario")
        print("4. Actualizar Usuario")
        print("5. Eliminar Usuario")
        print("6. Volver al menu del Administrador")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            break
        else:
            print("Opcion invalida, intente otra vez")

