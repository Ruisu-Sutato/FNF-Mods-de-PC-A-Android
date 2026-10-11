import os
from convertir import Convertidor
from fileControlador import File
from dialogos import Dialogos
from character import ConvertirChar
from estructura import Estructuras
print(" Bienvenido ".center(63, "-"))
print("Opciones:\nhelp - Instrucciones para el uso del programa.\nconvertir - Convertir el mod de PC a Android.\ndiálogos - Convierte los diálogos de PC a Android.\npersonaje - Convierte un personaje a Android.\nestructura - Crea una estructura de un mod convencional de FNF de Android.\nWeek - Convierte las semanas de PC a Android")

enMod = False
if os.path.exists("Mi Mod"):
    enMod = True if input("Deseas guardar los archivos en la estructura actual? Si/No : ").lower() == "si" else False
    print("Los archivos se guardaran en la estructura Mi Mod." if enMod else "Los archivos aparaceran fuera de la estructura.")
while True:
    opciones = input("Ingresa la opción: ").replace("á", "a").lower()

    if opciones == "help":
        print("\nPara convertir un archivo de PC a Android debes ingresar la url del archivo de la canción y luego el archivo de eventos correspondiente. Si el archivo de eventos no existe el programa no añadirá ningún evento.\n\nPara convertir los diálogos solo ingrese la url del archivo de diálogos.")
    elif opciones == "convertir" :
        archivo  = File.leerJson(input("Ingresa la url del archivo que deseas convertir. \n"))

        archivoEvents = File.leerJson(input("Ingresa la url del archivo de eventos. \n")) or {"events" : [], "format" : "psych_v1"}

        metadata = Convertidor.metadata(archivo)
        chart = Convertidor.chart(archivo, archivoEvents)
        carpeta = f"{metadata['songName'].lower().replace(' ', '-')}-android"
        if enMod:
            carpeta = f"Mi Mod/data/songs/{carpeta}"
        File.guardarJson(metadata, metadata["songName"] + "-metadata", carpeta)
        File.guardarJson(chart, metadata["songName"] + "-chart", carpeta)
    elif opciones == "dialogos":
        nombreArchivo = input("Como se llama la canción en la que aparcen estos dialogos? Esto se usara para el nombre del archivo.\n") or "mis-dialogos"
        nombreArchivo = nombreArchivo.lower().replace(" ", "-")
        dialogos = Dialogos.convertirDialogos(File.leerJson(input("Ingresa la url del los diálogos qué deseas convertir a Android.\n")))
        carpeta = "diálogos-android"
        if enMod:
            carpeta = "Mi Mod/data/dialogue/conversations"
        File.guardarJson(dialogos, nombreArchivo, carpeta)
    elif opciones == "personaje":
        url =  File.leerJson(input("Ingresa la url del personaje qué deseas convertir a Android.\n"))
        tipo = input("Que tipo de personaje es. NPC como senpai, BF o GF.\n")
        nombreArchivo = input("Como se llama el personaje? Esto se usara para el nombre del archivo.\n") or "nuevoPersonaje"
        carpeta = "Personajes"
        personaje = False
        if tipo.lower() == "npc":
            personaje = ConvertirChar.npc(url, nombreArchivo)
        elif tipo.lower() == "bf":
            personaje = ConvertirChar.bf(url, nombreArchivo)
        elif tipo.lower() == "gf":
            personaje = ConvertirChar.gf(url, nombreArchivo)
        else: 
            print("Ese tipo de personaje no existe.")
        if personaje:
            if enMod:
                carpeta = "Mi Mod/data/characters"
            File.guardarJson(personaje, nombreArchivo.replace(" ", "-"), carpeta)
    elif opciones == "estructura":
        Estructuras.mod()
        print("Estructura creada.")
        enMod = True if input("Deseas guardar los archivos en la estructura actual? Si/No : ").lower() == "si" else False
        print("Los archivos se guardaran en la estructura Mi Mod." if enMod else "Los archivos aparaceran fuera de la estructura.")
    elif opciones == "week":
        archivo = File.leerJson(input("Ingresa la url de la Week que deseas convertir.\n"))
        archivo, nombre = Convertidor.week(archivo)
        nombre = F"week{nombre.replace(' ', '')}"
        carpeta = "New Week"
        if enMod:
            carpeta = "Mi Mod/data/levels"
        File.guardarJson(archivo, nombre, carpeta)