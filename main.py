from convertir import Convertidor
from jsonControlador import JsonControl

archivo  = JsonControl.leerJson(input("Ingresa la url del archivo que deseas convertir. \n"))

archivoEvents = JsonControl.leerJson(input("Ingresa la url del archivo de eventos. \n"))

archivo = archivo["song"] if not isinstance(archivo["song"], str) else archivo

metadata = Convertidor.metadata(archivo)
chart = Convertidor.chart(archivo, archivoEvents)

JsonControl.guardarJson(metadata,                 metadata["songName"] + "-metadata")
JsonControl.guardarJson(chart, metadata["songName"] + "-chart")    