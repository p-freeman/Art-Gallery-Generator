import os
import shutil
import markdown
import html
import re

def generate_gallery_html(image_folder, intro_text='', captions=None):
    """
    Generates HTML code for a static art gallery webpage with lightbox feature.

    Args:
    - image_folder (str): Path to the folder containing images.
    - intro_text (str): Introductory text to be displayed above the gallery.
    - captions (dict): A dictionary where keys are image filenames and values are captions for the images.

    Returns:
    - gallery_html (str): HTML code for the gallery webpage.
    """
    gallery_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Art Gallery</title>
        <style>
            /* Add CSS styles for gallery layout */
            .intro-text {
                font-family: sans-serif;
            }
            .gallery {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
                gap: 10px;
            }
            .gallery img {
                max-width: 100%;
                max-height: 200px;
            }
            .lb-caption {
                font-family: Arial, sans-serif;
            }
            /* Add your custom styles here */
        </style>
        <link rel="stylesheet" href="lightbox.min.css"> <!-- Lightbox CSS -->
    </head>
    <body>
    """

    if intro_text:
        gallery_html += f"""
        <div class="intro-text">
            {markdown.markdown(intro_text)}
        </div>
        <hr>
        """

    gallery_html += """
        <div class="gallery">
    """

    # Sort images based on their order in the captions file
    sorted_images = sorted(os.listdir(image_folder), key=lambda x: list(captions.keys()).index(x) if x in captions else float('inf'))

    for filename in sorted_images:
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            caption = captions.get(filename, '') if captions else ''
            # Convert Markdown to HTML
            caption_html = markdown.markdown(caption)
            # Escape HTML special characters
            caption_html = html.escape(caption_html)
            caption_html = caption_html.replace('"', '&quot;')
            # Escape quotation marks in the title attribute
            caption_html = caption_html.replace("'", "&apos;")
            gallery_html += f"""
            <a href="images/{filename}" data-lightbox="gallery" data-title="{caption_html}">
                <img src="images/{filename}" alt="{filename}" title="{caption.replace('"', '&quot;').replace("'", '&apos;')}">
            </a>
            """

    gallery_html += """
        </div>
        <script src="lightbox-plus-jquery.min.js"></script> <!-- Lightbox JavaScript -->
    </body>
    <!--
    LICENSE
    Lightbox2 is licensed under The MIT License.
    100% Free. Lightbox is free to use in both commercial and non-commercial work.
    Attribution is required. This means you must leave my name, my homepage link, and the license info intact. None of these items have to be user-facing and can remain within the code.
    Attribution:
    Lightbox by Lokesh Dhakar (https://lokeshdhakar.com)
    -->
    </html>
    """

    return gallery_html

def save_html(html_content, output_path):
    """
    Save HTML content to a file.

    Args:
    - html_content (str): HTML content to be saved.
    - output_path (str): Path to save the HTML file.
    """
    with open(output_path, 'w') as f:
        f.write(html_content)

def load_captions_from_file(captions_file):
    """
    Load captions from a text file.

    Args:
    - captions_file (str): Path to the text file containing captions.

    Returns:
    - captions (dict): A dictionary where keys are image filenames and values are captions for the images.
    """
    captions = {}
    with open(captions_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                filename, caption = parts
                captions[filename.strip()] = caption.strip()
    return captions

def generate_gallery():
    """
    Generates the gallery webpage, copies images, and saves it.
    """
    script_folder = os.path.dirname(__file__)
    input_folder = os.path.join(script_folder, "input")
    output_folder = os.path.join(script_folder, "output")

    # Delete output folder if it exists
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    # Create output folder
    os.makedirs(output_folder)

    images_folder = os.path.join(input_folder, "images")
    captions_file = os.path.join(script_folder, "captions.txt")
    intro_text_file = os.path.join(input_folder, "intro.md")

    if not os.path.exists(images_folder):
        print("Images folder not found.")
        return

    intro_text = ''
    if os.path.exists(intro_text_file):
        with open(intro_text_file, 'r') as f:
            intro_text = f.read()

    captions = {}
    if os.path.exists(captions_file):
        captions = load_captions_from_file(captions_file)

    output_images_folder = os.path.join(output_folder, "images")
    os.makedirs(output_images_folder, exist_ok=True)  # Create output images folder if it doesn't exist

    # Copy images to the output folder
    for filename in os.listdir(images_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            src = os.path.join(images_folder, filename)
            dst = os.path.join(output_images_folder, filename)
            shutil.copy2(src, dst)

    gallery_html = generate_gallery_html(output_images_folder, intro_text, captions)
    save_html(gallery_html, os.path.join(output_folder, "index.html"))

    # Copy Lightbox files to the output folder
    dist_folder = os.path.join(script_folder, "dist")
    if os.path.exists(dist_folder):
        shutil.copy(os.path.join(dist_folder, "css", "lightbox.min.css"), output_folder)
        shutil.copy(os.path.join(dist_folder, "js", "lightbox-plus-jquery.min.js"), output_folder)

    print("Gallery generated successfully.")

if __name__ == "__main__":
    generate_gallery()
