from database.conexion import get_connection


class RolController:

    @staticmethod
    def listar():
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

    @staticmethod
    def buscar(texto):
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM tblroles WHERE strdescripcion ILIKE %s",
                        (f"%{texto}%",),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar rol: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(descripcion):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO tblroles (strdescripcion) VALUES (%s)",
                        (descripcion,),
                    )
            return True
        except Exception as e:
            print(f"Error al crear rol: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_rol, descripcion):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "UPDATE tblroles SET strdescripcion = %s WHERE idrolempleado = %s",
                        (descripcion, id_rol),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar rol: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_rol):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tblroles WHERE idrolempleado = %s",
                        (id_rol,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar rol: {e}")
            return False
        finally:
            conexion.close()