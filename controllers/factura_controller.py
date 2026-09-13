from database.conexion import get_connection


class FacturaController:

    @staticmethod
    def listar():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM spconsultafactura()")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar facturas: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def crear(fecha, idcliente, idempleado, descuento, iva, total, idestado, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tblfactura
                            (dtmfecha, idcliente, idempleado, numdescuento, numiva,
                             numtotal, idestado, dtmfechamodifica, strusuariomodifico)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, now(), %s)
                        """,
                        (fecha, idcliente, idempleado, descuento, iva, total, idestado, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al crear factura: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def actualizar(id_factura, fecha, idcliente, idempleado, descuento, iva, total, idestado, usuario):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "CALL actualizar_factura(%s, %s, %s, %s, %s, %s, %s, %s, now(), %s)",
                        (id_factura, fecha, idcliente, idempleado, descuento,
                         iva, total, idestado, usuario),
                    )
            return True
        except Exception as e:
            print(f"Error al actualizar factura: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def eliminar(id_factura):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tbldetalle_factura WHERE idfactura = %s",
                        (id_factura,),
                    )
                    cursor.execute(
                        "DELETE FROM tblfactura WHERE idfactura = %s",
                        (id_factura,),
                    )
            return True
        except Exception as e:
            print(f"Error al eliminar factura: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def listar_clientes():
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
    def listar_empleados():
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
    def listar_estados():
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT * FROM tblestado")
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar estados: {e}")
            return []
        finally:
            conexion.close()

    @staticmethod
    def agregar_detalle(id_factura, id_producto, cantidad, precio):
        conexion = get_connection()
        if conexion is None:
            return False

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO tbldetalle_factura
                            (idfactura, idproducto, numcantidad, numprecio)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (id_factura, id_producto, cantidad, precio),
                    )
            return True
        except Exception as e:
            print(f"Error al agregar detalle de factura: {e}")
            return False
        finally:
            conexion.close()

    @staticmethod
    def listar_detalle(id_factura):
        conexion = get_connection()
        if conexion is None:
            return []

        try:
            with conexion:
                with conexion.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT d.idproducto, p.strnombre, d.numcantidad, d.numprecio
                        FROM tbldetalle_factura d
                        JOIN tblproducto p ON p.idproducto = d.idproducto
                        WHERE d.idfactura = %s
                        """,
                        (id_factura,),
                    )
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error al listar detalle de factura: {e}")
            return []
        finally:
            conexion.close()