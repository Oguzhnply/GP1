from PIL import Image
import os
from glob import glob



def convert_png_to_ico(png_folder, ico_output_folder):
    # Check if the 'icon' subfolder exists, if not create it
    icon_folder = os.path.join(ico_output_folder, 'icon')
    if not os.path.exists(icon_folder):
        os.mkdir(icon_folder)

    # Get a list of PNG files in the specified folder
    png_files = glob(os.path.join(png_folder, '*.png'))

    if not png_files:
        print("No PNG files found in the specified folder.")
        return

    for png_file in png_files:
        try:
            # Open each PNG file
            img = Image.open(png_file)

            # Get the path and filename without extension
            path, filename = os.path.split(png_file)
            name, ext = os.path.splitext(filename)

            # Create ICO filename and path in the 'icon' subfolder
            ico_path = os.path.join(icon_folder, f'{name}.ico')

            # Save as ICO
            img.save(ico_path, format='ICO')

            print(f"Converted {png_file} to {ico_path}")

        except Exception as e:
            print(f"Error converting {png_file}: {e}")

    print("Success")

# Example usage
png_folder = r'C:\Users\Oguzhan\Desktop\gp1\output\1'
ico_output_folder = r'C:\Users\Oguzhan\Desktop\gp1\output'

# Test the function
convert_png_to_ico(png_folder, ico_output_folder)

