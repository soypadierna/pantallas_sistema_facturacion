import os

ESTRUCTURA = {
    "views": {
        "__init__.py": None,
        "login_window.py": None,
        "principal_window.py": None,
        "clientes": ["lista_clientes_window.py", "cliente_window.py"],
        "productos": ["lista_productos_window.py", "producto_window.py"],
        "categorias": ["lista_categorias_window.py", "categoria_window.py"],
        "facturas": ["lista_facturas_window.py", "factura_window.py"],
        "informes": ["informes_window.py"],
        "empleados": ["lista_empleados_window.py", "empleado_window.py"],
        "roles": ["lista_roles_window.py", "rol_window.py"],
        "seguridad": ["seguridad_window.py"],
        "ayuda": ["ayuda_window.py", "acerca_de_window.py"],
    },
    "models": ["cliente.py", "producto.py", "categoria.py", "factura.py", "empleado.py", "rol.py"],
    "controllers": [
        "cliente_controller.py",
        "producto_controller.py",
        "categoria_controller.py",
        "factura_controller.py",
        "empleado_controller.py",
        "rol_controller.py",
    ],
    "database": ["conexion.py"],
    "utils": ["validaciones.py"],
}


def crear_archivo(ruta):
    if not os.path.exists(ruta):
        open(ruta, "w").close()


def crear_paquete(carpeta, contenido):
    os.makedirs(carpeta, exist_ok=True)
    crear_archivo(os.path.join(carpeta, "__init__.py"))

    if isinstance(contenido, list):
        for archivo in contenido:
            crear_archivo(os.path.join(carpeta, archivo))

    elif isinstance(contenido, dict):
        for nombre, sub in contenido.items():
            if nombre == "__init__.py":
                continue
            ruta = os.path.join(carpeta, nombre)
            if isinstance(sub, (list, dict)):
                crear_paquete(ruta, sub)
            else:
                crear_archivo(ruta)


def main():
    crear_archivo("main.py")
    crear_archivo("requirements.txt")

    for carpeta, contenido in ESTRUCTURA.items():
        crear_paquete(carpeta, contenido)

    os.makedirs("assets", exist_ok=True)
    with open("assets/.gitkeep", "w") as f:
        f.close()

    print("Estructura creada correctamente.")


if __name__ == "__main__":
    main()
    