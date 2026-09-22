class Eventos:
    def convertirEventos(datos, events):
            eventos = []
            for seccion in datos:
                must = seccion.get("mustHitSection", False)
                eventos.append({ "t": 0 if len(seccion["sectionNotes"]) == 0 else seccion["sectionNotes"][0][0] , "e": "FocusCamera", "v": { "char": 0 if must else 1, "x": 0, "y": 0 } })          
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