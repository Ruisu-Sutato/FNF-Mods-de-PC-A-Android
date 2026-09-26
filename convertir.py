from eventos import Eventos

class Convertidor:
    def metadata(datos):
        if isinstance(datos["notes"], dict):
            dificultades = {k: 5 for k in datos["notes"]}
            dificultades2 = list(datos["notes"])
        else:
            dificultades = {"normal" : 5}
            dificultades2 = ["normal"]
        print("Metadata convertida con exito!")
        return {
        "version" : "2.2.4",
        "songName" : datos.get("song", "Canción"), 
        "artist" : "Alguien",
        "charter" : "Alguien",
        "offsets" : {} if datos.get("offset", {}) == 0 else datos.get("offset", {}),
        "playData" : {
        "difficulties" : dificultades2,
        "characters" : {
        "player" : datos.get("player1", "bf"),
        "girlfriend" : datos.get("gfVersion", ""),
        "opponent" : datos.get("player2", ""),
        "opponentVocals" : [datos.get("player2", "")],
        "playerVocals" : [datos.get("player1", "bf")],
        },
        "stage" : datos.get("stage", "mainStageErect"),
        "noteStyle" : "pixel" if datos.get("player1", "bf").endswith("pixel") else "funkin",
        "ratings" :dificultades,
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

    def chart(datos, events, multi = False):
        eventos = Eventos.convertirEventos(datos.get("notes", []), events)
        cancion = []
        if isinstance(datos.get("notes", []), list):
            velocidad = {"normal" : datos.get("speed", 1)}
            for notas in datos.get("notes", []):
                must = notas.get("mustHitSection", False)
            #alt = notas.get("altAnim", False)
                for teclas in notas.get("sectionNotes", []):
                    d = teclas[1]
                    if not must and multi:
                        d = (d + 4) % 8
                    cancion.append({ "t": teclas[0], "d": d, "l": teclas[2]})             
            dificultades = {"normal" : cancion}
            print(f"Chart convertido con exito!\nCantidad de notas : {len(cancion)}")
        else:
                velocidad = datos.get("speed", 1)
                dificultades = {k: [] for k in datos["notes"]}
                for dificultad, secciones in datos["notes"].items():
                    for seccion in secciones:
                        must = seccion.get("mustHitSection", False)
                        for teclas in seccion["sectionNotes"]:
                            d = teclas[1]
                            if not must:
                                d = (d + 4) % 8
                            dificultades[dificultad].append({ "t": teclas[0], "d": d, "l": teclas[2]})
                                    
                                      
        return { "version" : "2.0.0",
        "scrollSpeed" : velocidad,
        "events" : eventos,
        "notes" : dificultades,
        "generatedBy" : "Luis Angel Solis Avila"}