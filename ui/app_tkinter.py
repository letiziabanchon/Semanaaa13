# ui/app_tkinter.py
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculo import Vehiculo

class AppTkinter(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Garaje - Registro de Vehículos")
        self.geometry("540x370")
        self.resizable(False, False)

        self._construir_formulario()
        self._construir_tabla()
        self._construir_botones()

    # ---------- UI ----------
    def _construir_formulario(self):
        frm = ttk.LabelFrame(self, text="Datos del vehículo")
        frm.pack(fill="x", padx=10, pady=10)

        ttk.Label(frm, text="Placa:").grid(row=0, column=0, padx=6, pady=6, sticky="e")
        ttk.Label(frm, text="Marca:").grid(row=1, column=0, padx=6, pady=6, sticky="e")
        ttk.Label(frm, text="Propietario:").grid(row=2, column=0, padx=6, pady=6, sticky="e")

        self.ent_placa = ttk.Entry(frm, width=25)
        self.ent_marca = ttk.Entry(frm, width=25)
        self.ent_prop = ttk.Entry(frm, width=25)
        self.ent_placa.grid(row=0, column=1, padx=6, pady=6)
        self.ent_marca.grid(row=1, column=1, padx=6, pady=6)
        self.ent_prop.grid(row=2, column=1, padx=6, pady=6)

    def _construir_tabla(self):
        cont = ttk.LabelFrame(self, text="Vehículos registrados")
        cont.pack(fill="both", expand=True, padx=10, pady=(0,10))

        cols = ("placa", "marca", "propietario")
        self.tabla = ttk.Treeview(cont, columns=cols, show="headings", height=7)
        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")
        self.tabla.column("placa", width=120)
        self.tabla.column("marca", width=160)
        self.tabla.column("propietario", width=200)
        self.tabla.pack(fill="both", expand=True, padx=8, pady=8)

    def _construir_botones(self):
        frm_btn = ttk.Frame(self)
        frm_btn.pack(fill="x", padx=10, pady=(0,10))

        ttk.Button(frm_btn, text="Agregar vehículo", command=self.on_agregar).pack(side="left", padx=5)
        ttk.Button(frm_btn, text="Limpiar campos", command=self.on_limpiar_campos).pack(side="left", padx=5)
        # Botón extra opcional: limpiar tabla (no es obligatorio, pero ayuda en pruebas)
        ttk.Button(frm_btn, text="Vaciar lista", command=self.on_vaciar_lista).pack(side="right", padx=5)

    # ---------- Eventos ----------
    def on_agregar(self):
        placa = self.ent_placa.get()
        marca = self.ent_marca.get()
        propietario = self.ent_prop.get()

        try:
            vehiculo = Vehiculo(placa, marca, propietario)
            self.servicio.agregar_vehiculo(vehiculo)
            self.tabla.insert("", tk.END, values=vehiculo.to_tuple())
            self.on_limpiar_campos()
        except ValueError as e:
            messagebox.showwarning("Validación", str(e))

    def on_limpiar_campos(self):
        for entry in (self.ent_placa, self.ent_marca, self.ent_prop):
            entry.delete(0, tk.END)
        self.ent_placa.focus()

    def on_vaciar_lista(self):
        if messagebox.askyesno("Confirmar", "¿Vaciar todos los registros del garaje?"):
            self.servicio.limpiar_registros()
            for item in self.tabla.get_children():
                self.tabla.delete(item)