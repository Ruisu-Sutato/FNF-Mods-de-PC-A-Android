from eventos import Eventos
import typing

class Convertidor:
    def metadata(datos = dict) -> dict:
        if not datos.get("format", False):
            datos = datos.get("song")
        if isinstance(datos["notes"], dict):
            ratings = {k: 5 for k in datos["notes"]}
            dificultades = list(datos["notes"])
        else:
            ratings = {"normal" : 5}
            dificultades = ["normal"]
        print("Metadata convertida con exito!")
        return {
        "version" : "2.2.4",
        "songName" : datos.get("song", "Canción"), 
        "artist" : "Alguien",
        "charter" : "Alguien",
        "offsets" : {} if datos.get("offset", {}) == 0 else datos.get("offset", {}),
        "playData" : {
        "difficulties" : dificultades,
        "characters" : {
        "player" : datos.get("player1", "bf"),
        "girlfriend" : datos.get("gfVersion", ""),
        "opponent" : datos.get("player2", ""),
        "opponentVocals" : [datos.get("player2", "")],
        "playerVocals" : [datos.get("player1", "bf")],
        },
        "stage" : datos.get("stage", "mainStageErect"),
        "noteStyle" : "pixel" if datos.get("player1", "bf").endswith("pixel") else "funkin",
        "ratings" : ratings,
         "album" : "volume2"
        },
            "generatedBy" : "Luis Angel Solis Avila",
          "timeChanges" : [{
          "t" : 0,
          "b" : 0,
          "bpm" : datos.get("bpm", 123),
          "bt" : [4, 4, 4, 4]
          }]
            }

    def chart(datos = dict, events = dict) -> dict:
        cancion = []
        formato = True
        if not datos.get("format", False):
            datos = datos.get("song")
            formato = False
        eventos = Eventos.convertir(datos.get("notes", []), events)
        if isinstance(datos.get("notes", []), list):
            velocidad = {"normal" : datos.get("speed", 1)}
            for notas in datos.get("notes", []):
                must = notas.get("mustHitSection", False)
                alt = notas.get("altAnim", False)
                for teclas in notas.get("sectionNotes", []):
                    cancion.append(identificar(teclas, alt, must, formato))    
            dificultades = {"normal" : cancion}
            print(f"Chart convertido con exito!\nCantidad de notas : {len(cancion)}")
        else:
                velocidad = datos.get("speed", 1)
                dificultades = {k: [] for k in datos["notes"]}
                for dificultad, secciones in datos["notes"].items():
                    for seccion in secciones:
                        alt = seccion.get("altAnim", False)
                        must = seccion.get("mustHitSection", False)
                        for teclas in seccion["sectionNotes"]:
                            dificultades[dificultad].append(identificar(teclas, alt, must, formato))
                            
                                    
                                      
        return { "version" : "2.0.0",
        "scrollSpeed" : velocidad,
        "events" : eventos,
        "notes" : dificultades,
        "generatedBy" : "Luis Angel Solis Avila"}

    def week(datos = dict) -> dict:
        nuevaWeek = {
            "version" : "1.0.0",
            "name" : datos.get("storyName", "New Week"),
            "capsule": {
            "name": datos.get("weekName", "New Week")
            },
            "titleAsset" : "storymenu/titles/week1",
            "props": [
    {
      "assetPath": "storymenu/props/dad",
      "scale": 1.0,
      "offsets": [100, 60],
      "animations": [
        {
          "name": "idle",
          "prefix": "idle0",
          "frameRate": 24
        }
      ]
    },
    {
      "assetPath": "storymenu/props/bf",
      "scale": 1.0,
      "offsets": [150, 80],
      "animations": [
        {
          "name": "idle",
          "prefix": "idle0",
          "frameRate": 24
        },
        {
          "name": "confirm",
          "prefix": "confirm0",
          "frameRate": 24
        }
      ]
    },
    {
      "assetPath": "storymenu/props/gf",
      "scale": 1.0,
      "offsets": [200, 80],
      "animations": [
        {
          "name": "danceLeft",
          "prefix": "idle0",
          "frameIndices": [30, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        },
        {
          "name": "danceRight",
          "prefix": "idle0",
          "frameIndices": [
            15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
          ]
        }
      ]
    }
  ],
  "background": "#F9CF51",
  "songs" : []
}

        for cancion in datos.get("songs"):
            nuevaWeek["songs"].append(cancion[0])
        
        return nuevaWeek, nuevaWeek["name"]

def identificar(teclas = list, alt = bool, must = bool, formato = bool)-> dict:
    d = teclas[1]
    if not must and not formato:
        d = (d + 4) % 8
    tecla = { "t": teclas[0], "d": d}
    if teclas[2] > 0:
        tecla.setdefault("l", teclas[2])
    if alt or teclas[-1] == "Alt Animation":
        tecla.setdefault("k", "mom")
    return tecla