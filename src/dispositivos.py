dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "VLAN"
    }
]

def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Protocolo:", dispositivo["protocolo"])

print("SISTEMA DE BÚSQUEDA DE DISPOSITIVOS")
busqueda = input("Ingrese el nombre del dispositivo: ")
encontrado = False

for dispositivo in dispositivos:
    if dispositivo["nombre"] == busqueda:
        print("\nDispositivo encontrado:")
        mostrar_dispositivo(dispositivo)
        
        if dispositivo["estado"] == "Activo":
            print("El dispositivo está disponible.")
        else:
            print("El dispositivo requiere atención.")
            
        encontrado = True
        break

if not encontrado:
    print("\nDispositivo no encontrado.")