while True:
    print("""
            Bienvenido al sistema de registro de empleados
            1. Registrar empleado
            2. Mostrar empleados
            3. Eliminar empleado.
            4. Lista de sueldos.
            5. Salir
        """)
    try:
        usuario = input(int("Ingrese una opcion: "))
        if usuario == 1:
            print("Proxima funcionalidad")
        elif usuario == 2:
            print("Proxima funcionalidad")
        elif usuario == 3:
            print("Proxima funcionalidad")
        elif usuario == 4:
            print("Proxima funcionalidad")
        elif usuario == 5:
            print("Gracias por usar el sistema, hasta la proxima.")
            break
    except ValueError:
        print("Ingrese un valor numerico correcto...")