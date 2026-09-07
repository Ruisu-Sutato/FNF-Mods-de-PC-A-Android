import json
import os

def forma1(datos):
     metadata = {
     "version" : "2.2.4",
     "songName" : nombreSong,
     "artist" : "Alguien",
     "charter" : "Alguien",
     "offsets" : datos.get("offset", {}),
     "playData" : {
     "difficulties" : dificultades,
     "characters" : {
     "player" : datos.get("player1", "bf"),
     "girlfriend" : datos.get("gfVersion", ""),
     "opponent" : datos.get("player2", ""),
     "opponentVocals" : [datos.get("player1", "bf")],
     "playerVocals" : [datos.get("player2", "")]
        },
     "stage" : datos.get("stage", "mainStageErect"),
     "noteStyle" : "pixel" if datos.get("player1", "bf").endswith("pixel") else "funkin",
     "ratings" : {
     "normal" : 5},
     "album" : "volume2",
     },
      "generatedBy" : "Luis Angel Solis Avila",
      "timeChanges" : [{
      "t" : 0,
      "b" : 0,
      "bpm" : datos.get("bpm", 123),
      "bt" : [4, 4, 4, 4]
      }]
        }
     cancion = []
     events = []
     for notas in datos.get("notes", []):
         alt = notas.get("altAnim", False)
         for teclas in notas.get("sectionNotes", []):
                 if not events:
                     events.append({
                     "t" : teclas[0],
                     "e" : "FocusCamera",
                     "v" : {
                     "char" : 1 if teclas[1] > 3 else 0
                     }
                     })
                 elif (teclas[1] > 3 and events[-1]["v"]["char"] != 1):
                     events.append({
                     "t" : teclas[0],
                     "e" : "FocusCamera",
                      "v" : {
                     "char" : 1
                     }
                     })
                 elif teclas[1] <= 3 and events[-1]["v"]["char"] != 0:
                     events.append({
                        "t" : teclas[0],
                        "e" : "FocusCamera",
                        "v" : {
                        "char" : 0
                        }
                        })
                    
                     if alt:
                        alt = "player3"
                        tecla = {"t" : teclas[0], "d" : teclas[1], "l" : teclas[2], "k" : alt}
                        cancion.append(tecla)
                     else:
                        tecla = {"t" : teclas[0], "d" : teclas[1], "l" : teclas[2]}
                        cancion.append(tecla)
    with open(rutaEvent, "r") as f:
            eventosJson = json.load(f)
            for evento in eventosJson["events"]:
                tiempo = evento[0]
                for parametros in evento[1]:
                    if parametros[0] == "Add Zoom Camera":
                        nombre = "ZoomCamera"
                        para = parametros[1:]
                        events.append(
                {"t" : tiempo, "e" : nombre,
                 "v" : {
                 "ease" : "elasticOut",
                 "duration" : float(para[1]) * 100,
                 "mode": "stage",
                 "zoom" : float(para[0]) * 50
                 }
                })       
    chart = {
        "version" : "2.0.0",
        "scrollSpeed" : {
        "hard" : datos.get("speed", 1.0)
        },
        "events" : events,
        "notes" : {
        "hard" : "cancion"
        },
        "generatedBy" : "Luis Angel Solis Avila"
        }
        
crearJson(chart, metadata["songName"])
crearJson(metadata, metadata["songName"])


def crearJson(archivo, nombre):
    nombreSong = nombre.lower().replace(" ", "-") or "canción"
    if not os.path.exists(f"{nombreSong}-android"):
        os.makedirs(f"{nombreSong}-android")
    with open(f"{nombreSong}-android/{nombreSong}-chart.json","w") as f:
        json.dump(archivo, f, indent = 2)
    print(f"Archivo guardado como {nombreSong}-chart.json")
    
    
    
try:
    ruta = input("Ingresa la ruta del archivo. ")
    rutaEvent = "events.json"#input("Ingresa la ruta del archivo de eventos. ")
    with open(ruta, "r") as f:
        datos = json.load(f)
        if isinstance(datos["song"], str):
            forma1(datos)
except FileNotFoundError:
    print("No se encontró el archivo.")
except KeyError as e:
    print(f"Json Inválido {e}")
except Exception as e:
    print(f"Error {e}")
    