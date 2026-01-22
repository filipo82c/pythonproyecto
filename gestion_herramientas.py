import json
import os

Archivo = "herramientas.json"

def cargar_herramientas():
    if not os.path.exists(Archivo):
        with open(Archivo, "w", encoding="utf-8") as f:
            json.dump([], f)          
    with open(Archivo, "r", encoding="utf-8") as f:
        return json.load(f)
    
def guardar_herramientas(herramientas):
    with open(Archivo, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, indent=4)
        
def crear_herramientas():
    herramientas = cargar_herramientas() 
    try:
        nueva = { "id": len(herramientas)+1,
                "nombre": input("nombre: "),
                "categoria":input("categoria: "),
                "cantidad": int(input("cantidad disponible: ")),
                "estado": "activa",
                "valor": float(input("valor estimado: "))}
    except ValueError:
        print("Error: Cantidad y valor deben ser numeros validos")
        return 
    herramientas.append(nueva)
    guardar_herramientas(herramientas)
    print("herramientas creadas correctamente")
     
def listar_herramientas():
    herramientas = cargar_herramientas()
    if not herramientas:
        print("no hay herramientas registradas")   
        return
    print("\\listado de herramientas:")
    for h in herramientas: 
        print(
            f"{h['id']} - {h['nombre']} | "
            f"{h['categoria']} | " 
            f"stock:  {h['cantidad']} | "
            f"estado: {h['estado']} | "
            f"valor: {h['valor']}  ")
        
def buscar_herramientas():
    herramientas = cargar_herramientas()
    try:
        id_buscar = int(input("ID de la herramienta: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    for h in herramientas:
        if h["id"] == id_buscar:
            print("Herramienta encontrada")
            print(h)
            return
    print("Herramienta no encontrada")
    
def eliminar_herramientas():
    herramientas = cargar_herramientas()
    id_eliminar = int(input("ID de las herramientas a eliminar: "))
    herramientas = [h for h in herramientas if h["id"] != id_eliminar] 
    guardar_herramientas(herramientas)
    print("herramientas eliminadas correctamente")
    
def inactivar_herramientas():
    herramientas = cargar_herramientas()
    try:
        id_buscar = int(input("ID de la herramienta a inactivar: "))
    except ValueError:
        return
    for h in herramientas:
        if h["id"] == id_buscar:
            h["estado"] = "fuera de servicio"
            guardar_herramientas(herramientas)
            print("herramientas inactivas correctamente")
            return
    print("herramientas no encontradas")    
    
def herramientas_menu():
    while True:
        print("\n--- Gestion de Herramientas ---")
        print("1. Crear herramientas")
        print("2. Listar herramientas")
        print("3. Buscar herramientas")
        print("4. Inactivar herramientas")
        print("5. Eliminar Herramientas")
        print("6. Volver al menu del administrador")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            crear_herramientas()
        elif opcion == "2":
            listar_herramientas()
        elif opcion == "3":
            buscar_herramientas()
        elif opcion == "4":
            inactivar_herramientas()
        elif opcion == "5":
            eliminar_herramientas()
        elif opcion == "6":
            break
        else:
            print("Opcion invalida, intente otra vez")  
            
def herramientas_stock_bajo(limite=3):
    herramientas = cargar_herramientas()
    print("\n=== Herramientas con Stock Bajo ===")
    bajo = [h for h in herramientas if h["cantidad"] < limite]
    if not bajo:
        print("No hay herramientas con stock bajo")
        return
    for h in bajo:
        print(f"ID: {['id']} | {h['nombre']} | "
              f"Stock: {h['cantidad']} | Estado: {h['estado']}")      
