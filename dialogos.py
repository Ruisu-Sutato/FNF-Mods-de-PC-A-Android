from jsonControlador import JsonControl
class Dialogos:
    def convertirDialogos(archivo):
        dialogos = []
        for dialogo in archivo["dialogue"]:
            dialogos.append({
            "speaker" : dialogo["portrait"],
            "speakerAnimation" : "talk",
            "box" : "roses",
            "boxAnimation": "idle",
            "text": [dialogo["text"]]
            }) 
    
        nuevoArchivo = {
            "version" : "1.0.0",
            "backdrop" : {
                "type" : "solid",
                "fadeTime" : 2.0,
                "color" : "#BFB3DFD8"
        },

            "music" : {
                "asset" : "",
                "fadeTime" : 0,
                "looped" : False
        },

            "outro" : {
            "type": "fade",
            "fadeTime": 1.0
            },
    
            "dialogue" : dialogos
        }
        print(f"Diálogos convertidos con exito!\nTotal de diálogos : {len(dialogos)}")
        JsonControl.guardarJson(nuevoArchivo, "diálogo", "diálogos")