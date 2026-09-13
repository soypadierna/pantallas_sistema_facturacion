from database.conexion import get_connection


class ProductoController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblproducto")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar productos: {e}")
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
                        SELECT * FROM tblproducto
                        WHERE strnombre ILIKE %s OR strcodigo ILIKE %s
                        """,
                        (f"%{texto}%", f"%{texto}%"),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar producto: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(nombre, codigo, preciocompra, precioventa, idcategoria, detalle, foto, stock, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblproducto
                            (strnombre, strcodigo, numpreciocompra, numprecioventa,
                             idcategoria, strdetalle, strfoto, numstock,
                             dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, now(), %s)
                        """,
                        (nombre, codigo, preciocompra, precioventa, idcategoria,
                         detalle, foto, stock, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al crear producto: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_producto, nombre, codigo, preciocompra, precioventa,
                    idcategoria, detalle, foto, stock, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_producto(%s, %s, %s, %s, %s, %s, %s, %s, now(), %s)",
                        (id_producto, nombre, codigo, preciocompra, precioventa,
                         idcategoria, detalle, foto, stock, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL eliminar_producto(%s)",
                        (id_producto,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def listar_categorias():
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