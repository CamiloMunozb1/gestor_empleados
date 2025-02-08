import sqlite3

# CLASE PARA LA CONEXIÓN A LA BASE DE DATOS
class ConexionDB:
    def __init__(self, ruta_db):
        try:
            # ESTABLECE LA CONEXIÓN CON LA BASE DE DATOS Y CREA UN CURSOR PARA EJECUTAR CONSULTAS
            self.conn = sqlite3.connect(ruta_db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"ERROR AL CONECTARSE A LA BASE DE DATOS: {error}")

    # MÉTODO PARA INSERTAR UN EMPLEADO EN LA TABLA
    def insertar_empleados(self):
        try:
            # SOLICITA AL USUARIO LOS DATOS DEL EMPLEADO
            Nombre_Empleado = str(input("Ingrese el nombre del empleado: "))
            Apellido_Empleado = str(input("Ingrese el apellido del empleado: "))
            puesto = str(input("Ingrese el puesto del empleado: "))
            salario = int(input("Ingrese el salario del empleado: "))

            # EJECUTA LA CONSULTA SQL PARA INSERTAR LOS DATOS EN LA TABLA EMPLEADOS
            self.cursor.execute("INSERT INTO Empleados (Nombre_Empleado, Apellido_Empleado, puesto, salario) VALUES (?,?,?,?)",
                                (Nombre_Empleado, Apellido_Empleado, puesto, salario))

            # GUARDA LOS CAMBIOS EN LA BASE DE DATOS
            self.conn.commit()
            print(f"Empleado {Nombre_Empleado} {Apellido_Empleado}, {puesto} registrado con éxito.")
        except ValueError:
            # MANEJO DE ERROR SI EL USUARIO INGRESA UN SALARIO NO NUMÉRICO
            print("ERROR: INGRESE UN SALARIO VÁLIDO (NÚMERO ENTERO).")
        except sqlite3.Error as error:
            # MANEJO DE ERRORES RELACIONADOS CON LA BASE DE DATOS
            print(f"ERROR AL INSERTAR EMPLEADO: {error}")

    # MÉTODO PARA MOSTRAR TODOS LOS EMPLEADOS REGISTRADOS
    def mostrar_empleados(self):
        try:
            # EJECUTA LA CONSULTA PARA OBTENER TODOS LOS EMPLEADOS
            self.cursor.execute("SELECT * FROM Empleados")
            empleados = self.cursor.fetchall()

            # SI HAY EMPLEADOS, LOS MUESTRA; SI NO, IMPRIME UN MENSAJE INDICANDO QUE NO HAY REGISTROS
            if empleados:
                for empleado in empleados:
                    print(empleado)
            else:
                print("NO HAY EMPLEADOS REGISTRADOS.")
        except sqlite3.Error as error:
            # MANEJO DE ERRORES EN LA CONSULTA SQL
            print(f"ERROR AL OBTENER EMPLEADOS: {error}")

    # MÉTODO PARA ELIMINAR UN EMPLEADO DE LA BASE DE DATOS
    def eliminar_empleados(self):
        try:
            # SOLICITA AL USUARIO EL NOMBRE Y APELLIDO DEL EMPLEADO A ELIMINAR
            Nombre_Empleado = str(input("Ingrese el nombre del empleado a eliminar: "))
            Apellido_Empleado = str(input("Ingrese el apellido del empleado a eliminar: "))

            # BUSCA EL ID DEL EMPLEADO EN LA BASE DE DATOS
            self.cursor.execute("SELECT Empleado_ID FROM Empleados WHERE Nombre_Empleado = ? AND Apellido_Empleado = ?", 
                                (Nombre_Empleado, Apellido_Empleado))
            id_empleado = self.cursor.fetchone()

            # SI EL EMPLEADO EXISTE, SE PROCEDE A ELIMINARLO; SI NO, SE MUESTRA UN MENSAJE DE ERROR
            if id_empleado:
                id_empleado = id_empleado[0]
                self.cursor.execute("DELETE FROM Empleados WHERE Nombre_Empleado = ? AND Apellido_Empleado = ?", 
                                    (Nombre_Empleado, Apellido_Empleado))
                self.conn.commit()
                print(f"Empleado {Nombre_Empleado}, {Apellido_Empleado} eliminado con éxito.")
            else:
                print("EMPLEADO NO ENCONTRADO.")
        except ValueError:
            # MANEJO DE ERROR SI EL USUARIO INGRESA UN DATO INCORRECTO
            print("ERROR: INGRESE UN NOMBRE Y APELLIDO VÁLIDOS.")
        except sqlite3.Error as error:
            # MANEJO DE ERRORES RELACIONADOS CON LA BASE DE DATOS
            print(f"ERROR AL ELIMINAR EMPLEADO: {error}")

    # MÉTODO PARA CERRAR LA CONEXIÓN A LA BASE DE DATOS
    def cerrar_conexion(self):
        try:
            self.conn.close()
            print("CONEXIÓN CERRADA EXITOSAMENTE.")
        except sqlite3.Error as e:
            print(f"ERROR AL CERRAR LA CONEXIÓN: {e}")

# CREACIÓN DE LA INSTANCIA DE LA CONEXIÓN A LA BASE DE DATOS
ruta_db = "C:/Users/POWER/ges_empleados.db.db"
conexion = ConexionDB(ruta_db)
