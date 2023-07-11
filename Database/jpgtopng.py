import os
from PIL import Image

def convert_to_png(input_folder):
    # Iterate through all files and folders in the input folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            # Check if the file is a JPG or JPEG image
            if file.lower().endswith(('.jpg', '.jpeg')):
                # Get the input file path
                input_path = os.path.join(root, file)
                
                try:
                    # Open the input image using Pillow
                    image = Image.open(input_path)
                    
                    # Convert the image to PNG format and save it
                    output_file = os.path.splitext(file)[0] + ".png"
                    output_path = os.path.join(root, output_file)
                    image.save(output_path, "PNG")
                    
                    print(f"Converted: {input_path} -> {output_path}")
                    
                    # Delete the original JPG/JPEG file
                    os.remove(input_path)
                    print(f"Deleted: {input_path}")
                except Exception as e:
                    print(f"Error converting: {input_path}")
                    print(str(e))

# Usage example
input_folder = "C:/Users/kosanam/OneDrive/Desktop/database6/55"

convert_to_png(input_folder)