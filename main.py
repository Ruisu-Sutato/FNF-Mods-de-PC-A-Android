from convertir import Convertidor
from jsonControlador import JsonControl
from dialogos import Dialogos
from character import ConvertirChar
print(" Bienvenido ".center(63, "-"))
print("Opciones:\nhelp - Instrucciones para el uso del programa.\nconvertir - Convertir el mod de PC a Android.\ndiálogos - Convierte los diálogos de PC a Android.\npersonaje - Convierte un personaje a Android.")

while True:
    opciones = input("Ingresa la opción: ").replace("á", "a").lower()

    if opciones == "help":
        print("\nPara convertir un archivo de PC a Android debes ingresar la url del archivo de la canción y luego el archivo de eventos correspondiente. Si el archivo de eventos no existe el programa no añadirá ningún evento.\n\nPara convertir los diálogos solo ingrese la url del archivo de diálogos.")
    elif opciones == "convertir" :
        archivo  = JsonControl.leerJson(input("Ingresa la url del archivo que deseas convertir. \n"))

        archivoEvents = JsonControl.leerJson(input("Ingresa la url del archivo de eventos. \n")) or {"events" : []}

        archivo = archivo["song"] if not isinstance(archivo["song"], str) else archivo

        metadata = Convertidor.metadata(archivo)
        chart = Convertidor.chart(archivo, archivoEvents)
        carpeta = metadata["songName"].lower().replace(" ", "-")
        JsonControl.guardarJson(metadata, metadata["songName"] + "-metadata", carpeta)
        JsonControl.guardarJson(chart, metadata["songName"] + "-chart", carpeta)
    elif opciones == "dialogos":
        Dialogos.convertirDialogos(JsonControl.leerJson(input("Ingresa la url del los diálogos qué deseas convertir a Android.\n")))
    elif opciones == "personaje":
        url =  JsonControl.leerJson(input("Ingresa la url del personaje qué deseas convertir a Android.\n"))
        tipo = input("Que tipo de personaje es. NPC como senpai, BF o GF.\n")
        if tipo.lower() == "npc":
            ConvertirChar.npc(url)
        elif tipo.lower() == "bf":
            ConvertirChar.bf(url)
        elif tipo.lower() == "gf":
            ConvertirChar.gf(url)
        else: 
            print("Ese tipo de personaje no existe.")