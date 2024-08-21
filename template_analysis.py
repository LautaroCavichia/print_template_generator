from PIL import Image
import json
import os


def analyze_template(model_name=None):
    # User input for model name
    if not model_name:
        model_name = input("Enter model name: ")
    image_path = f"templates/{model_name}.png"

    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    image = Image.open(image_path)
    pixels = image.load()
    total_width, total_height = image.size

    # Initialize coordinates for the red area
    red_x_min = red_y_min = float('inf')
    red_x_max = red_y_max = 0

    # Find the coordinates of the red area
    for y in range(total_height):
        for x in range(total_width):
            r, g, b, a = pixels[x, y]
            if r > 200 and g < 50 and b < 50:  # Condition to identify red color
                if x < red_x_min:
                    red_x_min = x
                if y < red_y_min:
                    red_y_min = y
                if x > red_x_max:
                    red_x_max = x
                if y > red_y_max:
                    red_y_max = y

    red_width = red_x_max - red_x_min + 1
    red_height = red_y_max - red_y_min + 1

    # Initialize the JSON structure if the file does not exist
    if not os.path.exists("misure_modelli.json"):
        with open("misure_modelli.json", "w") as f:
            json.dump({"modelli": {}}, f, indent=4)

    # Load existing data
    with open("misure_modelli.json", "r") as f:
        data = json.load(f)

    # Update the model data
    data["modelli"][model_name] = {
        "width": red_width,
        "height": red_height
    }

    # Save the updated data back to the JSON file with indentation
    with open("misure_modelli.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Red area dimensions: width={red_width}, height={red_height}")

