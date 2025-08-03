import csv
from datetime import datetime

ARCHIVO = "turnos.csv"

def cargar_turnos():
    try:
        with open(ARCHIVO, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def guardar_turno(turno):
    existe = False
    try:
        with open(ARCHIVO, newline='', encoding='utf-8') as f:
            existe = True
    except FileNotFoundError:
        pass

    with open(ARCHIVO, 'a', newline='', encoding='utf-8') as f:
        campos = ['nombre', 'fecha', 'hora', 'servicio']
        writer = csv.DictWriter(f, fieldnames=campos)

        if not existe:
            writer.writeheader()
        writer.writerow(turno)

def mostrar_turnos(turnos):
    if not turnos:
        print("No hay turnos cargados.")
    else:
        print("\nTurnos agendados:")
        for t in turnos:
            print(f"- {t['fecha']} {t['hora']}: {t['nombre']} ({t['servicio']})")

def buscar_turnos_por_nombre(turnos, nombre):
    return [t for t in turnos if nombre.lower() in t['nombre'].lower()]

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def menu():
    while True:
        print("\n--- Sistema de Turnos para Peluquería ---")
        print("1. Agregar turno")
        print("2. Ver todos los turnos")
        print("3. Buscar turno por nombre")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre del cliente: ").strip()
            if not nombre:
                print("❌ El nombre no puede estar vacío.")
                continue

            fecha = input("Fecha (DD-MM-AAAA): ").strip()
            if not validar_fecha(fecha):
                print("❌ Fecha inválida. Usá el formato correcto.")
                continue

            hora = input("Hora (HH:MM): ").strip()
            if not validar_hora(hora):
                print("❌ Hora inválida. Usá el formato 24 hs (ej: 14:30).")
                continue

            servicio = input("Servicio (ej: corte, peinado, etc.): ").strip()
            if not servicio:
                print("❌ El servicio no puede estar vacío.")
                continue
            turno = {
                'nombre': nombre,
                'fecha': fecha,
                'hora': hora,
                'servicio': servicio
            }

            guardar_turno(turno)
            print("✅ Turno guardado.")

        elif opcion == "2":
            turnos = cargar_turnos()
            mostrar_turnos(turnos)

        elif opcion == "3":
            nombre = input("Nombre del cliente a buscar: ")
            turnos = cargar_turnos()
            encontrados = buscar_turnos_por_nombre(turnos, nombre)
            mostrar_turnos(encontrados)

        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción inválida. Intentalo de nuevo.")

menu()