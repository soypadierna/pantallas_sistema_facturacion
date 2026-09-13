from database.conexion import get_connection


class CategoriaController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM tblcategoria_prod")
            resultados = cursor.fetchall()
            return resultados
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
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT * FROM tblcategoria_prod WHERE strdescripcion ILIKE %s",
                (f"%{texto}%",),
            )
            resultados = cursor.fetchall()
            return resultados
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
            cursor = conexion.cursor()
            cursor.execute(
                "CALL actualizar_categoriaprod(%s, %s, %s)",
                (None, descripcion, usuario),
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear categoría: {e}")
            conexion.rollback()
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_categoria, descripcion, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "CALL actualizar_categoriaprod(%s, %s, %s)",
                (id_categoria, descripcion, usuario),
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar categoría: {e}")
            conexion.rollback()
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_categoria):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "CALL eliminar_categoriaproducto(%s)",
                (id_categoria,),
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar categoría: {e}")
            conexion.rollback()
            return False
        finally:
            conexion.close()