import tkinter as tk
from tkinter import ttk, messagebox
from controllers.seguridad_controller import SeguridadController


class PrincipalWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("400x300")
        ttk.Label(self, text="Bienvenido", font=("Arial", 16)).pack(pady=20)


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x180")
        self.resizable(False, False)
        self._crear_widgets()

    def _crear_widgets(self):
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Usuario:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_usuario = ttk.Entry(frame)
        self.entry_usuario.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Clave:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_clave = ttk.Entry(frame, show="*")
        self.entry_clave.grid(row=1, column=1, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=20)

        self.btn_validar = ttk.Button(btn_frame, text="Validar", command=self.validar)
        self.btn_validar.pack(side="left", padx=5)

        self.btn_cancelar = ttk.Button(btn_frame, text="Cancelar", command=self.destroy)
        self.btn_cancelar.pack(side="left", padx=5)

    def validar(self):
        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()

        idempleado = SeguridadController.validar_login(usuario, clave)

        if idempleado is not None:
            self.destroy()
            principal = PrincipalWindow()
            principal.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o clave incorrectos")


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()