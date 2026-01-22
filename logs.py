from datetime import datetime
Archivo_log = "logs.txt"
def registrar_evento(mensaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(Archivo_log, "a", encoding="utf-8") as f:
        f.write(f"[{fecha}] {mensaje}\n")
    