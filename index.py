from funcionalidad.empleados import ConexionDB
ruta = "C:/Users/POWER/ges_empleados.db.db"
conexion = ConexionDB(ruta)


while True:
    print("""
            Bienvenido al sistema de registro de empleados
            1. Registrar empleado
            2. Mostrar empleados
            3. Eliminar empleado.
            4. Salir
        """)
    try:
        usuario = int(input("Ingrese una opcion: "))
        if usuario == 1:
            conexion.insertar_empleados()
        elif usuario == 2:
            conexion.mostrar_empleados()
        elif usuario == 3:
            conexion.eliminar_empleados()
        elif usuario == 4:
            print("Gracias por usar el sistema, hasta la proxima.")
            break
    except ValueError:
        print("Ingrese un valor numerico correcto...")