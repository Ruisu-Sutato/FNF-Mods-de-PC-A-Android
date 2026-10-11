from fileControlador import File
class Estructuras:
    def mod():
        File.crearCarpetas("Mi Mod/data/characters/Tus Personajes.txt", "Aqui tienes que colocar los archivos de tus personjes.")
        File.crearCarpetas("Mi Mod/data/levels/Tus Week.txt", "Aqui tienes que colocar los archivos de las semanas.")
        File.crearCarpetas("Mi Mod/data/dialogue/conversations/Tus dialogos.txt", "Aqui tienes que colocar tus archivos de dialogos.")
        File.crearCarpetas("Mi Mod/data/songs/Tus Archivos de canciones.txt", "Aqui debes colocar la carpeta de la cancion con sus respectivos archivos por ejemplo :\n\nmi-cancion/\n mi-cancion-metadata.json\n mi-cancion-chart.json")
        File.crearCarpetas("Mi Mod/images/icons/Tus Iconos.txt", "Aqui debes colocar los iconos de tus personajes.")
        File.crearCarpetas("Mi Mod/shared/images/characters/Las Imagenes de tus personajes.txt", "Aqui debes colocar las imagenes y xml de tus personajes.")
        File.crearCarpetas("Mi Mod/songs/Tus Archivos de ogg.txt", "Aqui debes colocar los archivos ogg.")
        File.crearCarpetas("Mi Mod/_polymod_meta.json", '{"title" : "Mi Mod", "description" : "Un mod para FNF.","contributors" : [{"neme" : "Luis Angel"}],"api_version" : "0.8.8","mod_version" : "1.0.0"}')