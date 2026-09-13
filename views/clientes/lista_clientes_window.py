import tkinter as tk
from tkinter import ttk, messagebox
from controllers.cliente_controller import ClienteController
from views.clientes.cliente_window import ClienteWindow


class ListaClientesWindow(tk.Toplevel):
    COLUMNAS = ("id", "nombre", "documento", "direccion", "telefono", "email")

    def __init__(self, master=None):
        super().__init__(master)
        self.title("Lista de Clientes")
        self.geometry("800x400")
        self._crear_widgets()
        self.cargar_clientes()

    def _crear_widgets(self):
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Buscar:").pack(side="left", padx=(0, 5))
        self.entry_buscar = ttk.Entry(top_frame)
        self.entry_buscar.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.btn_buscar = ttk.Button(top_frame, text="Buscar", command=self.buscar_clientes)
        self.btn_buscar.pack(side="left", padx=5)

        self.btn_nuevo = ttk.Button(top_frame, text="Nuevo", command=self.abrir_nuevo)
        self.btn_nuevo.pack(side="left", padx=5)

        self.btn_editar = ttk.Button(top_frame, text="Editar", command=self.abrir_editar)
        self.btn_editar.pack(side="left", padx=5)

        self.btn_borrar = ttk.Button(top_frame, text="Borrar", command=self.borrar_cliente)
        self.btn_borrar.pack(side="left", padx=5)

        tree_frame = ttk.Frame(self, padding=10)
        tree_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=self.COLUMNAS, show="headings")
        for col in self.COLUMNAS:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<Double-1>", lambda event: self.abrir_editar())

    def cargar_clientes(self):
        clientes = ClienteController.listar()
        self._llenar_tree(clientes)

    def buscar_clientes(self):
        texto = self.entry_buscar.get()
        clientes = ClienteController.buscar(texto)
        self._llenar_tree(clientes)

    def _llenar_tree(self, clientes):
        self.tree.delete(*self.tree.get_children())
        for cliente in clientes:
            self.tree.insert("", "end", values=cliente)

    def _obtener_seleccion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un cliente")
            return None
        return self.tree.item(seleccion[0], "values")

    def abrir_nuevo(self):
        ventana = ClienteWindow(self, modo="nuevo")
        self.wait_window(ventana)
        self.cargar_clientes()

    def abrir_editar(self):
        datos = self._obtener_seleccion()
        if datos is None:
            return

        cliente_id = datos[0]
        ventana = ClienteWindow(self, modo="editar", cliente_id=cliente_id, datos=datos)
        self.wait_window(ventana)
        self.cargar_clientes()

    def borrar_cliente(self):
        datos = self._obtener_seleccion()
        if datos is None:
            return

        cliente_id = datos[0]
        if messagebox.askyesno("Confirmar", "¿Desea eliminar este cliente?"):
            if ClienteController.eliminar(cliente_id):
                self.cargar_clientes()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el cliente")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = ListaClientesWindow(root)
    root.mainloop()