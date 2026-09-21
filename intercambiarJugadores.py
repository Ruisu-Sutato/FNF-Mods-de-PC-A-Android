from jsonControlador import JsonControl

class Intercambiar:
    def chart(chart):
        eventos = []
        for evento in chart["events"]:
            if isinstance(evento["v"], dict) and evento["v"].get("char", False):
                evento["v"]["char"] = 0 if evento["v"]["char"] else 1
                eventos.append(evento)
            elif isinstance(evento["v"], int):
                evento["v"] = 0 if evento["v"] else 1
                eventos.append(evento)
            elif evento.get("e", False) == "PlayAnimation":
                evento["v"]["target"] = "dad" if evento["v"]["target"] == "boyfriend" else "boyfriend"
                eventos.append(evento)
            else:
                eventos.append(evento)

        dificultades = list(chart["notes"])
        notas = {}
        for dificultad in dificultades:
            notas.setdefault(dificultad,  [])
            for nota in chart["notes"][dificultad]:
                nota["d"] = nota["d"] - 4 if nota["d"] > 3 else nota["d"] + 4
                notas[dificultad].append(nota)

        print(f"Exito al intercambiar jugadores\nTotal de eventos : {len(eventos)}\nTotal de Notas {len(notas[dificultades[-1]])}")
        JsonControl.guardarJson({
            "version" : chart.get("version", "2.0.0"),
            "scrollSpeed" : chart.get("scrollSpeed", 0),
            "events" : eventos,
            "notes" : notas,
            "generatedBy" : "Luis Angel"
        }, "intercambio", "intercambio")

