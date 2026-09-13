from database.conexion import get_connection


class SeguridadController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblseguridad")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar seguridad: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(idempleado, usuario, clave, modificador):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblseguridad
                            (idempleado, strusuario, strclave, dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, %s, %s, now(), %s)
                        """,
                        (idempleado, usuario, clave, modificador),
                    )
            return True
        except Exception as e:
            print(f"Error al crear seguridad: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(idempleado, usuario, clave, modificador):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_seguridad(%s, %s, %s, now(), %s)",
                        (idempleado, usuario, clave, modificador),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar seguridad: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(idempleado):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL eliminar_seguridad(%s)",
                        (idempleado,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar seguridad: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def validar_login(usuario, clave):
        conexion = get_connection()
        if conexion is None:
            return None

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT idempleado FROM tblseguridad WHERE strusuario = %s AND strclave = %s",
                        (usuario, clave),
                    )
                    resultado = cursor.fetchone()
                    return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al validar login: {e}")
            return None
        finally:
            conexion.close()