from PIL import Image, ImageDraw
import json

def generate_iphone_template(phone_name, cover_image_path, width_px, height_px):
    # Dimensioni del piano di stampa
    canvas_width = 3507
    canvas_height = 4960

    # Coordinate per posizionare l'immagine della cover
    start_x = 625
    start_y = 472

    # Distanza dal bordo sinistro per la linea nera
    black_line_x = 13

    # Carica l'immagine della cover e ridimensiona
    cover_image = Image.open(cover_image_path).convert("RGBA")
    cover_image = cover_image.resize((width_px, height_px))

    # Crea un canvas trasparente
    canvas = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))

    # Crea una linea nera
    draw = ImageDraw.Draw(canvas)
    line_y_start = start_y  # La linea inizia all'altezza del rettangolo rosso
    line_y_end = start_y + height_px  # La linea finisce all'altezza del rettangolo rosso
    draw.line([(black_line_x, line_y_start), (black_line_x, line_y_end)], fill="black", width=1)

    # Posiziona l'immagine della cover sul canvas
    canvas.paste(cover_image, (start_x, start_y), cover_image)

    # Salva l'immagine finale
    filename = f"{phone_name}_template.png"
    canvas.save(filename)
    print(f"Template saved as {filename}")


#usa i modelli in misure_modelli.json
#carica i modelli da misure_modelli.json
with open("misure_modelli.json", "r") as f:
    phone_models = json.load(f)["modelli"]


#genera template di ip14_promax
generate_iphone_template("ip14_promax", "prova.jpg", phone_models["ip14_promax"]["width"], phone_models["ip14_promax"]["height"])

