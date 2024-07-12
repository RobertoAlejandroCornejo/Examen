from utilidades import *

# Ejecución del programa
sueldos = []

while True:
    print("\nMenu:")
    print("1) Asignar sueldos aleatorios")
    print("2) Clasificar sueldos")
    print("3) Ver estadisticas")
    print("4) Reporte de sueldos")
    print("5) Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        asignar_sueldos(sueldos)
    elif opcion == '2':
        clasificar_sueldos(sueldos)
    elif opcion == '3':
        ver_estadistica(sueldos)
    elif opcion == '4':
        reporte_sueldos(sueldos)
    elif opcion == '5':
        salir_del_programa(sueldos)
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
