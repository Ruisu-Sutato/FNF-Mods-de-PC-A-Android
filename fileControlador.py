import json
import os
import typing
class File:
    def leerJson(url=str) -> dict:
        try:
            with open(url, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return datos
        except FileNotFoundError:
            print("No se encontró el archivo.")
        except KeyError as e:
            print(f"Json Inválido {e}")
        except Exception as e:
            print(f"Error {e}2")

    def guardarJson(archivo=dict ,nombre=str, carpeta=str):
        try:
            nombre = nombre.lower().replace(" ", "-")
            if not os.path.exists(f"{carpeta}"):
                os.makedirs(f"{carpeta}")
            with open(f"{carpeta}/{nombre}.json", "w", encoding="utf-8") as f:
                json.dump(archivo,  f,  indent=4)
                print(f"Archivo guardado como {nombre}.json")
        except FileNotFoundError:
            print("No se encontró el archivo.")
        except KeyError as e:
            print(f"Json Inválido {e}")
        except Exception as e:
            print(f"Error {e}")

    def crearCarpetas(url = str, archivo = None or str):
        os.makedirs(os.path.dirname(url), exist_ok=True)
        with open(url, "w", encoding="utf-8") as f:
            f.write(archivo)