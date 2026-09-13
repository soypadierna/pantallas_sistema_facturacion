from database.conexion import get_connection


class EmpleadoController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblempleado")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar empleados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def buscar(texto):
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM tblempleado WHERE strnombre ILIKE %s",
                        (f"%{texto}%",),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar empleado: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(nombre, documento, direccion, telefono, email, idrol, ingreso, retiro, datos, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblempleado
                            (strnombre, numdocumento, strdireccion, strtelefono, stremail,
                             idrolempleado, dtmfechaingreso, dtmfecharetiro, strdatosadicionales,
                             dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, now(), %s)
                        """,
                        (nombre, documento, direccion, telefono, email, idrol,
                         ingreso, retiro, datos, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al crear empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_empleado, nombre, documento, direccion, telefono, email,
                    idrol, ingreso, retiro, datos, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_empleado(%s, %s, %s, %s, %s, %s, %s, %s, %s, now(), %s)",
                        (id_empleado, nombre, documento, direccion, telefono, email,
                         idrol, ingreso, retiro, datos, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_empleado):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL eliminar_empleado(%s)",
                        (id_empleado,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def listar_roles():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblroles")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar roles: {e}")
            return []
        finally:
            conexion.close()