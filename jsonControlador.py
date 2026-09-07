import json
import os
class JsonControl:
    def leerJson(url):
        try:
            with open(url, "r") as f:
                datos = json.load(f)
                return datos
        except FileNotFoundError:
            print("No se encontró el archivo.")
        except KeyError as e:
            print(f"Json Inválido {e}")
        except Exception as e:
            print(f"Error {e}2")

    def guardarJson(archivo ,nombre):
        try:
            nombre = nombre.lower().replace(" ", "-")
            carpeta = nombre.replace("-metadata", "").replace("-chart", "")
            if not os.path.exists(f"{carpeta}-android"):
                os.makedirs(f"{carpeta}-android")
            with open(f"{carpeta}-android/{nombre}-android.json", "w") as f:
                json.dump(archivo,  f,  indent=1)
                print(f"Archivo guardado como {nombre}.json")
        except FileNotFoundError:
            print("No se encontró el archivo.")
        except KeyError as e:
            print(f"Json Inválido {e}")
        except Exception as e:
            print(f"Error {e}")                