# Importamos la clase ConexionDB desde el módulo funcionalidad.empleados
from funcionalidad.empleados import ConexionDB

# Especificamos la ruta de la base de datos
ruta = "C:/Users/POWER/ges_empleados.db.db"

# Creamos una instancia de la clase ConexionDB con la ruta de la base de datos
conexion = ConexionDB(ruta)

# Iniciamos un bucle infinito para mantener el programa en ejecución hasta que el usuario decida salir
while True:
    # Mostramos el menú de opciones al usuario
    print("""
            Bienvenido al sistema de registro de empleados
            1. Registrar empleado
            2. Mostrar empleados
            3. Eliminar empleado
            4. Salir
        """)
    try:
        # Solicitamos al usuario que ingrese una opción del menú
        usuario = int(input("Ingrese una opción: "))
        
        # Verificamos la opción ingresada y llamamos al método correspondiente
        if usuario == 1:
            # Opción para registrar un nuevo empleado
            conexion.insertar_empleados()
        elif usuario == 2:
            # Opción para mostrar la lista de empleados
            conexion.mostrar_empleados()
        elif usuario == 3:
            # Opción para eliminar un empleado existente
            conexion.eliminar_empleados()
        elif usuario == 4:
            # Opción para salir del programa
            print("Gracias por usar el sistema, hasta la próxima.")
            break  # Rompemos el bucle while para finalizar el programa
        else:
            # Si el usuario ingresa un número fuera de las opciones válidas
            print("Por favor, ingrese un número entre 1 y 4.")
    except ValueError:
        # Capturamos la excepción si el usuario ingresa un valor que no es un número entero
        print("Ingrese un valor numérico correcto...")
