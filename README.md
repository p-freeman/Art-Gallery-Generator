# Art Gallery Generator

This script generates a static art gallery webpage with a lightbox feature. It allows you to create a gallery from a folder of images, along with optional introductory text and captions for the images.

## Requirements

- Python 3.x
- Markdown (Python library)

## Folder Structure

To use the script, ensure the following folder structure:

project_folder/
│
├── input/
│ ├── images/ # Folder containing images
│ ├── captions.txt # Text file containing image captions
│ └── intro.md # Markdown file with introductory text
│
└── output/ # Output folder for the generated gallery


## How to Use

1. Place your images in the `input/images` folder.
2. Optionally, create a Markdown file with introductory text in the `input` folder named `intro.md`.
3. Optionally, create a text file named `captions.txt` in the `input` folder to provide captions for your images. Each line should be in the format `filename: caption`.
4. Run the script. It will generate the gallery webpage in the `output` folder.

## Gallery Layout

The gallery webpage displays images in a grid layout with a maximum size of 200x200 pixels. Clicking on an image opens it in a lightbox for a larger view.

## Lightbox

The gallery utilizes the Lightbox library for the lightbox feature. Lightbox is licensed under [The MIT License](https://lokeshdhakar.com/projects/lightbox2/#license).

- 100% Free. Lightbox is free to use in both commercial and non-commercial work.
- Attribution is required. This means you must leave the name of Lokesh Dhakar, his homepage link (https://lokeshdhakar.com), and the license info intact. None of these items have to be user-facing and can remain within the code.

## Running the Script

1. Ensure you have Python installed on your system.
2. Navigate to the project directory containing the script.
3. Run the following command in your terminal or command prompt:

python art_gallery_generator.py

## Note

-   Ensure that you have the `Markdown` library installed (`pip install markdown`) before running the script.
-   Make sure your image filenames have appropriate extensions (e.g., `.jpg`, `.jpeg`, `.png`, `.gif`).
-   For best results, use high-quality images.
