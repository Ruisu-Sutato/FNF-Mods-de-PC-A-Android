class Eventos:
    def convertirEventos(datos, events):
            eventos = []
            for seccion in datos:
                for teclas in seccion["sectionNotes"]:
                    if not eventos:
                        eventos.append(
                    { "t": 0, "e": "FocusCamera", "v": { "char": 1 if teclas[1] > 3 else 0, "x": 0, "y": 0 } })
                    elif (teclas[1] > 3 and eventos[-1]["v"]["char"] != 1):
                         eventos.append({
                          "t" : teclas[0],
                           "e" : "FocusCamera",
                           "v" : {
                           "char" : 1
                            }
                            })
                    elif teclas[1] <= 3 and eventos[-1]["v"]["char"] != 0:
                            eventos.append({
                             "t" : teclas[0],
                             "e" : "FocusCamera",
                             "v" : {
                             "char" : 0
                              }
                              })                
            for evento in events.get("events", []):
                if evento[1][-1][0] == "Add Camera Zoom":
                    eventos.append(
                    {"t" : evento[0], "e" : "ZoomCamera", "v" : { "duration": float(evento[1][-1][-1]), "ease": "expoOut", "mode": "stage", "zoom":  float(evento[1][-1][1])* 50}
                  }  )
                else:
                    eventos.append(
                    {"t" : evento[0], "e" : evento[1][-1][0], "v" : { "v1": evento[1][-1][1], "v2":  evento[1][-1][-1]}
                  }  )
            print(f"Eventos convertidos con exito!\nTotal de eventos : {len(eventos)}")
            return eventos                       