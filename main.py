# main.py
from servicio.garaje_servicio import GarajeServicio
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    servicio = GarajeServicio()
    app = AppTkinter(servicio)
    app.mainloop()