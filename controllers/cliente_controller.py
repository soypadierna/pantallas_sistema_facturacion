from database.conexion import get_connection


class ClienteController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblclientes")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar clientes: {e}")
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
                        """
                        SELECT * FROM tblclientes
                        WHERE strnombre ILIKE %s OR numdocumento::text ILIKE %s
                        """,
                        (f"%{texto}%", f"%{texto}%"),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar cliente: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(nombre, documento, direccion, telefono, email, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblclientes
                            (strnombre, numdocumento, strdireccion, strtelefono,
                             stremail, dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, %s, %s, %s, %s, now(), %s)
                        """,
                        (nombre, documento, direccion, telefono, email, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_cliente, nombre, documento, direccion, telefono, email, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_cliente(%s, %s, %s, %s, %s, %s, %s, now())",
                        (id_cliente, nombre, documento, direccion, telefono, email, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_cliente):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL eliminar_cliente(%s)",
                        (id_cliente,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False
        finally:
            conexion.close()