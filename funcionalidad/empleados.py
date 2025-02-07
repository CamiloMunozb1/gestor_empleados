import sqlite3

# CLASE PARA CONEXION A BASE DE DATOS.
class ConexionDB:
    def __init__(self, ruta_db):
        # ESTABLECE LA CONEXION A LA BASE DE DATOS Y CREA EL CURSOR.
        self.conn = sqlite3.connect(ruta_db)
        self.cursor = self.conn.cursor()

    # METODO PARA INSERTAR ELEMENTOS EN LA TABLA DE EMPLEADOS.
    def insertar_empleados(self):
        Nombre_Empleado = str(input("Ingrese el nombre del empleado: "))
        Apellido_Empleado = str(input("Ingrese el apellido del empleado: "))
        puesto = str(input("Ingrese el puesto del empleado: "))
        salario = int(input("Ingrese el salario del empleado: "))
        self.cursor.execute("INSERT INTO Empleados (Nombre_Empleado, Apellido_Empleado, puesto, salario) VALUES (?,?,?,?)",(Nombre_Empleado, Apellido_Empleado, puesto, salario))
        self.conn.commit()
        print(f"Empleado {Nombre_Empleado} {Apellido_Empleado}, {puesto} registrado con exito.")

    # METODO PARA MOSTRAR LOS ELEMENTOS DE LA TABLA DE EMPLEADOS.
    def mostrar_empleados(self):
        self.cursor.execute("SELECT * FROM Empleados")
        return self.cursor.fetchall()

    # METODO PARA ELIMINAR ELEMENTOS DE LA TABLA DE EMPLEADOS.
    def eliminar_empleados(self):
        Nombre_Empleado = str(input("Ingrese el nombre del empleado a eliminar: "))
        Apellido_Empleado = str(input("Ingrese el apellido del empleado a eliminar: "))
        self.cursor.execute("DELETE FROM Empleados WHERE Nombre_Empleado = ? AND Apellido_Empleado = ?", (Nombre_Empleado, Apellido_Empleado))
        self.conn.commit()
        print(f"Empleado {Nombre_Empleado}, {Apellido_Empleado} eliminado con exito.")

    # METODO PARA CERRAR LA CONEXION A LA BASE DE DATOS.
    def cerrar_conexion(self):
        self.conn.close()

# INSTANCIAS PARA CONEXION A BASE DE DATOS.
ruta_db = "C:/Users/POWER/ges_empleados.db.db"
conexion = ConexionDB(ruta_db)
    
