import tkinter as tk
from tkinter import ttk, messagebox
from controllers.cliente_controller import ClienteController


class ClienteWindow(tk.Toplevel):
    def __init__(self, master=None, modo="nuevo", cliente_id=None, datos=None, on_success=None):
        super().__init__(master)
        self.modo = modo
        self.cliente_id = cliente_id
        self.on_success = on_success

        self.title("Nuevo Cliente" if modo == "nuevo" else "Editar Cliente")
        self.geometry("400x350")
        self.resizable(False, False)

        self._crear_widgets()

        if modo == "editar" and datos:
            self._precargar_datos(datos)

    def _crear_widgets(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nombre = ttk.Entry(frame)
        self.entry_nombre.grid(row=0, column=1, pady=5)
        self.lbl_error_nombre = ttk.Label(frame, text="", foreground="red")
        self.lbl_error_nombre.grid(row=1, column=1, sticky="w")

        ttk.Label(frame, text="Documento:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_documento = ttk.Entry(frame)
        self.entry_documento.grid(row=2, column=1, pady=5)
        self.lbl_error_documento = ttk.Label(frame, text="", foreground="red")
        self.lbl_error_documento.grid(row=3, column=1, sticky="w")

        ttk.Label(frame, text="Dirección:").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_direccion = ttk.Entry(frame)
        self.entry_direccion.grid(row=4, column=1, pady=5)

        ttk.Label(frame, text="Teléfono:").grid(row=5, column=0, sticky="w", pady=5)
        self.entry_telefono = ttk.Entry(frame)
        self.entry_telefono.grid(row=5, column=1, pady=5)

        ttk.Label(frame, text="Email:").grid(row=6, column=0, sticky="w", pady=5)
        self.entry_email = ttk.Entry(frame)
        self.entry_email.grid(row=6, column=1, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=20)

        self.btn_actualizar = ttk.Button(
            btn_frame,
            text="Actualizar" if self.modo == "editar" else "Guardar",
            command=self.guardar,
        )
        self.btn_actualizar.pack(side="left", padx=5)

        self.btn_cancelar = ttk.Button(btn_frame, text="Cancelar", command=self.destroy)
        self.btn_cancelar.pack(side="left", padx=5)

    def _precargar_datos(self, datos):
        # datos = (id, nombre, documento, direccion, telefono, email)
        self.entry_nombre.insert(0, datos[1])
        self.entry_documento.insert(0, datos[2])
        self.entry_direccion.insert(0, datos[3] or "")
        self.entry_telefono.insert(0, datos[4] or "")
        self.entry_email.insert(0, datos[5] or "")

    def _validar(self):
        valido = True
        self.lbl_error_nombre.config(text="")
        self.lbl_error_documento.config(text="")

        if not self.entry_nombre.get().strip():
            self.lbl_error_nombre.config(text="El nombre es obligatorio")
            valido = False

        if not self.entry_documento.get().strip():
            self.lbl_error_documento.config(text="El documento es obligatorio")
            valido = False

        return valido

    def guardar(self):
        if not self._validar():
            return

        nombre = self.entry_nombre.get().strip()
        documento = self.entry_documento.get().strip()
        direccion = self.entry_direccion.get().strip()
        telefono = self.entry_telefono.get().strip()
        email = self.entry_email.get().strip()
        usuario = "admin"

        if self.modo == "nuevo":
            exito = ClienteController.crear(nombre, documento, direccion, telefono, email, usuario)
        else:
            exito = ClienteController.actualizar(
                self.cliente_id, nombre, documento, direccion, telefono, email, usuario
            )

        if exito:
            messagebox.showinfo("Éxito", "Cliente guardado correctamente")
            if self.on_success:
                self.on_success()
            self.destroy()
        else:
            messagebox.showerror("Error", "No se pudo guardar el cliente")