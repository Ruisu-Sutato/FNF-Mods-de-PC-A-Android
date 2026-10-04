import typing

class Eventos:
    def convertir(datos = dict, events = dict) -> dict:
            eventos = []
            if not events.get("format", False):
                events = events.get("song")
            if isinstance(datos, dict):
                dificultades = list(datos)
                for dificultad in dificultades:
                    for seccion in datos[dificultad]:
                        must = seccion.get("mustHitSection", False)
                        eventos.append({ "t": 0 if len(seccion["sectionNotes"]) == 0 else seccion["sectionNotes"][0][0],
                        "e": "FocusCamera", "v": { "char": 0 if must else 1, "x": 0, "y": 0 }})
            else:
                for seccion in datos:
                    must = seccion.get("mustHitSection", False)
                    eventos.append({ "t": 0 if len(seccion["sectionNotes"]) == 0 else seccion["sectionNotes"][0][0],
                    "e": "FocusCamera", "v": { "char": 0 if must else 1, "x": 0, "y": 0 } })        
            for evento in events.get("events", []):
                tiempo = evento[0]
                print(evento)
                for accion in evento[1]:
                    print(accion)
                    eventos.append(identificar(tiempo, accion))
            print(f"Eventos convertidos con exito!\nTotal de eventos : {len(eventos)}")
            return eventos

def identificar(tiempo = int, eventos = list[str]) -> dict:
    if eventos[0] == "Add Camera Zoom":
        return {"t" : tiempo, "e" : "ZoomCamera", 
        "v" : { "duration": float(eventos[2]) if eventos[2] != '' else 0,
        "ease": "expoOut", "mode": "stage", "zoom":  float(eventos[1])* 50}}
    elif eventos[0] == "Play Animation":
        target = "bf"
        if eventos[2] == "2" or eventos[2] == "Dad":
            target = "dad"
        elif eventos[2] == "1" or eventos[2] == "BF":
            target = "bf"
        elif eventos[2] == "GF":
            target = "gf"
        else:
            target = eventos[2]
        return {"t": tiempo,
        "e": "PlayAnimation",
        "v": { "anim": eventos[1], "force": True, "target": target}}
    else:
        return {"t" : tiempo, "e" : eventos[0], "v" : { "v1": eventos[1], "v2":  eventos[2]}}
