from database.conexion import get_connection


class CategoriaController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblcategoria_prod")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar categorías: {e}")
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
                        "SELECT * FROM tblcategoria_prod WHERE strdescripcion ILIKE %s",
                        (f"%{texto}%",),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar categoría: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(descripcion, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblcategoria_prod
                            (strdescripcion, dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, now(), %s)
                        """,
                        (descripcion, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al crear categoría: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_categoria, descripcion, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_categoriaprod(%s, %s, now(), %s)",
                        (id_categoria, descripcion, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar categoría: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_categoria):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL eliminar_categoriaproducto(%s)",
                        (id_categoria,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar categoría: {e}")
            return False
        finally:
            conexion.close()