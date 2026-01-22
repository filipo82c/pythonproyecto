import os
import json
from datetime import datetime, timedelta
import gestion_herramientas 
from logs import registrar_evento

registrar_evento("Prueba de log funcionando")
Archivo = "prestamos.json"

def cargar_prestamos():
    if not os.path.exists(Archivo):
        with open(Archivo, "w", encoding="utf-8") as f:
            return json.dump([], f)
        with open(Archivo, "r", encoding="utf-8") as f:
            return json.load(f)
             
def guardar_prestamos(prestamos):
    with open(Archivo, "w", encoding="utf-8") as f:
        json.dump(prestamos, f, indent=4)
        
def crear_prestamo(usuario_id):
    prestamos = cargar_prestamos()
    herramientas_lista = gestion_herramientas.cargar_herramientas()
    try:
        id_herramienta = int(input("ID de la herramienta a prestar: ")) 
        cantidad_solicitada = int(input("Cantidad a solicitar"))
    except ValueError:
        print("Debe ingresar un numero valido")
        return    
    herramienta = next((h for h in herramientas_lista if h["id"] == id_herramienta),None)
    if not herramienta:
        print("Herramienta no encontrada")
        return
    prestamo = {
        "id": len(prestamos)+1,
        "id_usuario": usuario_id,
        "id_herramienta": id_herramienta,
        "cantidad": cantidad_solicitada,
        "fecha_inicio": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "fecha_devolucion_estimada": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M"),
        "estado": "pendiente",
        "observaciones": input("Observaciones (opcional): ")}
    prestamos.append(prestamo)
    guardar_prestamos(prestamos)
    print("Prestamo registrado correctamente ")
    print("Solicitud de prestamo creada, el administrador debe autorizar")
    registrar_evento(f"Solcitud de prestamo creada | Usuario: {usuario_id} |"
                  f"Herramienta: {id_herramienta} | Cantidad {cantidad_solicitada}")
    
def ver_historial(usuario_id):
    prestamos = cargar_prestamos()
    prestamos_usuario = [p for p in prestamos if p["id_usuario"] == usuario_id]
    if not prestamos_usuario:
        print("No hay prestamos registrados para este usuario")
        return
    print(f"\nHistorial de prestamos del usuario {usuario_id}:")
    for p in prestamos_usuario:
        print("-" * 60)
        print(
            f"ID: {p['id']} | Herramienta: {p['id_herramienta']} | "
            f"Cantidad: {p['cantidad']} | Estado: {p['estado']} | "
            f"Inicio: {p['fecha_inicio']} | Estimada: {p['fecha_devolucion_estimada']}" +
            (f" | Devuelto: {p.get('fecha_devolucion_real', '-')}" if p['estado']=="devuelto" else ""))

def aprobar_prestamo():
    prestamos = cargar_prestamos()
    herramientas_lista = gestion_herramientas.cargar_herramientas()
    pendientes = [p for p in prestamos if p["estado"] == "pendiente"]
    if not pendientes:
        print("No hay prestamos pendientes")
        return
    for p in pendientes:
        print(f"ID: {p['id']} | Usuario: {p['id_usuario']} | Herramienta: {p['id_herramienta']} | Cantidad: {p['cantidad']}")
    try:
        id_solicitud = int(input("Ingrese el ID del prestamo a aprobar: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    prestamo = next((p for p in prestamos if p["id"] == id_solicitud), None)
    if not prestamo:
        print("Prestamo no encontrado")
        return
    herramienta = next((h for h in herramientas_lista if h ["id"] == prestamo ["id_herramienta"]), None)
    if herramienta["cantidad"] < prestamo["cantidad"]:
        print(f"No hay suficiente stock, Solicitud rechazada por insuficiente stock")
        prestamo["estado"] = "rechazado"
        registrar_evento(f"Prestamo ID {prestamo['id']} rechazado por falta de stock | Usuario: {prestamo['id_usuario']} | Herramienta: {prestamo['id_herramienta']} | Cantidad: {prestamo['cantidad']}")
    else:
        herramienta["cantidad"] -= prestamo["cantidad"]
        prestamo["estado"] = "aprobado"
        print("Prestamo aprobado")   
    registrar_evento(f"Prestamo Aprobado | Usuario: {prestamo['id_usuario']} | " 
                  f"Herramienta: {prestamo['id_herramienta']} | Cantidad: {prestamo['cantidad']}")
    gestion_herramientas.guardar_herramientas(herramientas_lista)
    guardar_prestamos(prestamos)
 
def rechazar_prestamo():
    prestamos = cargar_prestamos()
    pendientes = [p for p in prestamos if p["estado"] == "pendiente"]
    if not pendientes:
        print("No hay prestamos pendientes")
        return
    for p in pendientes:
        print(f"ID: {p['id']} | Usuario: {p['id_usuario']} | Herramienta: {p['id_herramienta']} | Cantidad: {p['cantidad']}")
    try:   
         id_solicitud = int(input("Ingrese el ID del prestamo a rechazar: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    prestamo = next((p for p in prestamos if p["id"] == id_solicitud), None)
    if not prestamo:
        print("Prestamo no encontrado")
        return
    prestamo["estado"] = "rechazado"
    print("Prestamo rechazado")
    guardar_prestamos(prestamos)
    registrar_evento(f"Prestamo Rechazado administrador | Usuario: {prestamo['id_usuario']}"
                  f"Herramienta: {prestamo['id_herramienta']}")

def devolver_herramienta():
    prestamos = cargar_prestamos()
    herramientas_lista = gestion_herramientas.cargar_herramientas()
    try:
        id_prestamo = int(input("ID del prestamo a devolver: "))
    except ValueError:
        print("Debe ingresar un numero valido")
        return
    prestamo = next((p for p in prestamos if p["id"] == id_prestamo), None)
    if not prestamo:
        print("Prestamo no encontrado")
        return
    if prestamo["estado"] != "aprobado":
        print("Solo se pueden devolver prestamos aprobados")
        return
    herramienta = next((h for h in herramientas_lista if h["id"] == prestamo["id_herramienta"]), None)
    if herramienta:
        herramienta["cantidad"] += prestamo["cantidad"]
        gestion_herramientas.guardar_herramientas(herramientas_lista)
    prestamo["estado"] = "devuelto"
    prestamo["fecha_devolucion_real"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    guardar_prestamos(prestamos)
    print("Prestamo devuelto de manera correcta")
    registrar_evento(f"Prestamo Devuelto | Usuario: {prestamo['id_usuario']} | "
                  f"Herramienta: {prestamo['id_herramienta']}")
    
def prestamos_menu(usuario_id=None, admin=False):
    while True:
        print("\n=== Menu de prestamos ===")
        if admin:
            print("1. Aprobar prestamo")
            print("2. Rechazar prestamo")
            print("3. Devolver herramienta")
            print("4. Ver el historial del usuario")
            print("5. Volver al memu principal")
        else:
            print("1. Solicitar prestamo")
            print("2. Ver mi historial")
            print("3. Volver al menu principal")
        opcion = input("Seleccione una opcion: ")
        if admin:
            if opcion == "1":
                aprobar_prestamo()
            elif opcion == "2":
                rechazar_prestamo()
            elif opcion == "3":
                devolver_herramienta()
            elif opcion == "4":
                if usuario_id is None:
                    print("Debe ingresar el ID del usuario para ver su historial")
                    try:
                        usuario_id = int(input("ID del usuario: "))
                    except ValueError:
                        usuario_id = None
                        print("ID no existe")
                        continue
                    ver_historial(usuario_id)
                elif opcion == "5":
                    break
                else:
                    print("Opcion no valida ")
            else:
                if opcion == "1":
                    if usuario_id is None:
                        print("Usuario no identificado")
                        break
                    crear_prestamo(usuario_id)
                elif opcion == "2":
                    ver_historial(usuario_id)
                elif opcion == "3":
                    break
                else:
                    print("Opcion no valida")
def prestamos_activos_vencidos():
    prestamos = cargar_prestamos()
    hoy = datetime.now()
    activos = []
    vencidos = []
    for p in prestamos:
        if p["estado"] == "aprobado":
            fecha_estimada = datetime.strptime(
                p["fecha_devolucion_estimada"], "%Y-%m-%d %H:%M")
            if fecha_estimada < hoy:
                vencidos.append(p)
            else:
                activos.append(p)
    print("\n === Prestamos Activos ===")
    if not activos:
        print("No hay prestamos activos")
    for p in activos:
        print(f"ID: {p['id']} | Usuarios: {p['id_usuario']} |"
              f"Herramienta: {p['id_herramienta']} |"
              f"Devuelve: {p['fecha_devolucion_estimada']}")
    print("\n=== Prestamos Vencidos ===")
    if not vencidos:
        print("No hay prestamos vencidos")
    for p in vencidos:
        print(f"ID: {p['id']} | Usuario: {p['id-usuario']} | "
              f"Herramienta: {p['id_herramienta']}"
              f"Debia devolver: {p['fecha_devolucion_estimada']}")
        
    
#print("Crear_prestamo existe:", callable(crear_prestamo))