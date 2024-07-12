import csv
import random

empleados = ["Juan Pérez","María García","Pedro Soto","Isabel Gómez","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

# Definimos una función para asignar sueldos aleatorios
def asignar_sueldos(sueldos):
    for i in range(10):
        sueldo = round(random.uniform(300000, 2500000))
        sueldos.append(sueldo)
        return sueldos

# Función para clasificar los sueldos
def clasificar_sueldos(sueldos):
    sueldos.sort()
    print(empleados)
    print(sueldos)

# Función para ver estadisticas
def ver_estadistica(sueldos):
    if sueldos:
        print("\nEstadisticas:")
        print(f"El sueldo mas bajo es: ${min(sueldos)}")
        print(f"El sueldo mas alto es: ${max(sueldos)}")
        print(f"El sueldo promedio es: ${sum(sueldos)/10:.2f}")
    else:
        print("No hay sueldos para calcular.")

def reporte_sueldos(sueldos):
    print("\nReporte de sueldos:")
    for sueldo in sueldos:
        print(f"Sueldo: ${sueldo}")
    

# Función para guardar los sueldos en un archivo CSV
def salir_del_programa(sueldos, filename='sueldos.csv'):
    if sueldos:
        with open(filename, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Sueldo"])
            for sueldo in sueldos:
                writer.writerow([sueldo])
        print(f"Sueldos guardados en el archivo {filename}")
    else:
        print("No hay sueldos para guardar.")

