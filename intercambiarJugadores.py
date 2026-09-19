from jsonControlador import JsonControl

class Intercambiar:
    def chart(chart):
        eventos = []
        for evento in chart["events"]:
            if evento.get("v", False):
                eventos.append({
                    "t" : evento["t"], "e" : evento["e"], "v" : {"char" : 0 if evento["v"]["char"] == 1 else 1}
                                })


        dificultades = list(chart["notes"])
        notas = {}
        for dificultad in dificultades:
            notas.setdefault(dificultad,  [])
            for nota in chart["notes"][dificultad]:
                notas[dificultad].append({
                    "t" : nota["t"], "d" : nota["d"] - 4 if nota["d"] > 3 else nota["d"] + 4, "l" : nota.get("l", 0)
                })

        JsonControl.guardarJson({
            "version" : chart.get("version", "2.0.0"),
            "scrollSpeed" : chart.get("scrollSpeed", 0),
            "events" : eventos,
            "notes" : notas,
            "generatedBy" : "Luis Angel"
        }, "intercambio")
        return eventos, notas


Intercambiar.chart( JsonControl.leerJson("roses-chart.json"))