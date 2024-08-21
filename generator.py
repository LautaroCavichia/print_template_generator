from PIL import Image, ImageDraw
import json
import subprocess

def generate_iphone_template(phone_name, cover_image_path, width_px, height_px):
    # Dimensioni del piano di stampa
    canvas_width = 3507
    canvas_height = 4960

    # Coordinate per posizionare l'immagine della cover
    start_x = 625
    start_y = 472

    # Distanza dal bordo sinistro per la linea nera
    black_line_x = 11

    # Carica l'immagine della cover e ridimensiona
    cover_image = Image.open(cover_image_path).convert("RGBA")
    #gira l'immagine di 90 gradi
    cover_image = cover_image.rotate(90, expand=True)
    cover_image = cover_image.resize((width_px, height_px))

    # Crea un canvas trasparente
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

    # Crea una linea nera
    draw = ImageDraw.Draw(canvas)
    line_y_start = start_y
    line_y_end = start_y + height_px
    draw.line([(black_line_x, line_y_start), (black_line_x, line_y_end)], fill="black", width=5)

    canvas.paste(cover_image, (start_x, start_y), cover_image)

    filename = f"{phone_name}_template.png"
    canvas.save(filename, dpi=(11811, 11811))

    # Aggiungi metadati con ExifTool tramite subprocess
    metadata_command = (
        f'exiftool -PixelsPerUnitX=11811 -PixelsPerUnitY=11811  -ResolutionUnit=meters -SRGBRendering=Perceptual '
        f'-Gamma=2.2 {filename}'
    )
    subprocess.run(metadata_command, shell=True)

    print(f"Template saved as {filename}")


with open("misure_modelli.json", "r") as f:
    phone_models = json.load(f)["modelli"]


#genera template di ip14_promax
generate_iphone_template("ip14_promax13", "prova.jpg", phone_models["ip14_promax"]["width"], phone_models["ip14_promax"]["height"])

