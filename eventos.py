class Eventos:
    def convertirEventos(datos, events):
            eventos = []
            for seccion in datos:
                must = seccion.get("mustHitSection", False)
                eventos.append({ "t": 0 if len(seccion["sectionNotes"]) == 0 else seccion["sectionNotes"][0][0] , "e": "FocusCamera", "v": { "char": 0 if must else 1, "x": 0, "y": 0 } })          
            for evento in events["song"].get("events", []):
                if evento[1][-1][0] == "Add Camera Zoom":
                    eventos.append(
                    {"t" : evento[0], "e" : "ZoomCamera", "v" : { "duration": float(evento[1][-1][-1]) if evento[1][-1][-1] != '' else 0,
                    "ease": "expoOut", "mode": "stage", "zoom":  float(evento[1][-1][1])* 50}
                  }  )
                elif evento[1][-1][0] == "Play Animation":
                    target = "bf"
                    if evento[1][-1][-1] == "2":
                        target = "dad"
                    elif evento[1][-1][-1] == "1":
                        target = "bf"
                    else:
                        target = evento[1][-1][-1]
                    eventos.append( {
      "t": evento[0],
      "e": "PlayAnimation",
      "v": { "anim": evento[1][-1][1], "force": True, "target": target}
    })
                else:
                    eventos.append(
                    {"t" : evento[0], "e" : evento[1][-1][0], "v" : { "v1": evento[1][-1][1], "v2":  evento[1][-1][-1]}
                  }  )
            print(f"Eventos convertidos con exito!\nTotal de eventos : {len(eventos)}")
            return eventos                       