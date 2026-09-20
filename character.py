from jsonControlador import JsonControl

class ConvertirChar:
    def npc(archivo):
        nuevoArchivo = {
            "version" : "1.0.0",
            "name" : "nuevoPersonaje",
            "assetPath" : archivo.get("image", "characters/bf"),
            "singTime" : archivo.get("sing_duration", 0),
            "isPixel" : False,
            "scale" : archivo.get("scale", 4),
            "healthIcon" : {
                "id": archivo.get("healthicon", "bf"),
                "isPixel": False
            },
             "animations": []
        }


        for animacion in archivo.get("animations", []):
            nuevoArchivo["animations"].append(
                {
                    "name" : animacion.get("anim", "bf"),
                    "prefix" : animacion.get("name", "bf"),
                    "offsets" : animacion.get("offsets", [0, 0])
                }
                )

        JsonControl.guardarJson(nuevoArchivo, "NPC", "NPC")


    def bf(archivo):
        nuevoArchivo = {
            "version" : "1.0.0",
            "name" : "nuevoPersonaje",
            "assetPath" : archivo.get("image", "characters/bf"),
            "flipX" : archivo.get("flip_x", False),
            "renderType": "multisparrow",
            "singTime" : archivo.get("sing_duration", 0),
            "scale" : archivo.get("scale", 4),
            "isPixel" : False,
            "healthIcon" : {
                "id": archivo.get("healthicon", "bf"),
                "isPixel": False
            },
             "animations": []
        }


        for animacion in archivo.get("animations", []):
            nuevoArchivo["animations"].append(
                {
                    "name" : animacion.get("anim", "bf"),
                    "prefix" : animacion.get("name", "bf"),
                    "offsets" : animacion.get("offsets", [0, 0])
                }
                )

        JsonControl.guardarJson(nuevoArchivo,"BF", "BF")


    def gf(archivo):
        nuevoArchivo = {
            "version" : "1.0.0",
            "name" : "nuevoPersonaje",
            "isPixel" : False,
            "assetPath" : archivo.get("image", "characters/bf"),
            "scale" : archivo.get("scale", 4),
            "isPixel" : False,
             "animations": []
        }


        for animacion in archivo.get("animations", []):
            nuevoArchivo["animations"].append(
                {
                    "name" : animacion.get("anim", "bf"),
                    "prefix" : animacion.get("name", "bf"),
                    "frameIndices" : animacion.get("indices", []),
                    "offsets" : animacion.get("offsets", [0, 0])
                }
                )

        JsonControl.guardarJson(nuevoArchivo, "GF" ,"GF")