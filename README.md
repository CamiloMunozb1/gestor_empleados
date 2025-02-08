# Gestor de Empleados

## Descripción
Este proyecto es un sistema de gestión de empleados basado en Python y SQLite. Permite registrar, mostrar y eliminar empleados de una base de datos de manera sencilla mediante una interfaz de consola.

## Características
- Registro de empleados con nombre, apellido, puesto y salario.
- Visualización de todos los empleados registrados.
- Eliminación de empleados por nombre y apellido.
- Manejo de errores para garantizar estabilidad y facilidad de uso.

## Requisitos
- Python 3.x
- Biblioteca `sqlite3` (incluida en la instalación estándar de Python)

## Instalación
1. Clona este repositorio o descarga el código fuente.
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Asegúrate de tener Python instalado en tu sistema.
3. No es necesario instalar dependencias adicionales, ya que `sqlite3` viene integrado con Python.

## Uso
1. Ejecuta el script principal:
   ```bash
   python main.py
   ```
2. Sigue las instrucciones en pantalla para:
   - Registrar un nuevo empleado.
   - Mostrar la lista de empleados registrados.
   - Eliminar un empleado.
   - Salir del programa.

## Estructura del Proyecto
```
/
├── funcionalidad/
│   ├── empleados.py  # Módulo con la clase de conexión a la base de datos y operaciones
├── main.py  # Archivo principal del programa
├── ges_empleados.db.db  # Base de datos SQLite
└── README.md  # Documentación del proyecto
```

## Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama con tu función o mejora (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y confírmalos (`git commit -m "Descripción de los cambios"`).
4. Sube los cambios a tu repositorio (`git push origin nueva-funcionalidad`).
5. Crea un pull request en este repositorio.

## Licencia
Este proyecto está bajo la licencia MIT. 

## Autor
- Juan Camilo Muñoz Bautista - Desarrollador del proyecto.

---

¡Gracias por usar el Gestor de Empleados! 🚀

