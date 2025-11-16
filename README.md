# CS361-Image-Microservice

This microservice uses "ImageMSVCRequest.txt" as a pipeline to request, by name, an image from the "Image Library" folder be saved into the "Loaded Image" folder with updated quality settings, then uses "ImageMSVCResponse.txt" as a pipeline to respond with the full path of that file for the requesting program to use.

# Setup
In your IDE terminal install with the following (designed for Python 3+):

pip install os-sys

pip install pathlib

pip install Pillow

If using a multiple versions of Python you may need to use pipX where X is your version of Python.

Download the "Image Microservice" zip file and extract the "Image Microservice v[x.x]" folder wherever you like within your project. This microservice can be used anywhere, but be sure to only extract it where other files/projects are not finicky about folder contents. Ideally this will be the root of your main project, or in parallel with the folder holding your main project.

Open Image_MSVC.py and update "FILEPATH" in the "main_directory" variable to the root of the "Image Microservice" folder (include the "Image Microservice" folder). Ensure slash formatting matches document, as of now this means using double backslashes \ \ between folders.

In "Image Library" add all your high fidelity images. It is recommended to use a simple, but consistent and clear naming scheme.

# How to use

To request an image, run the Image Microservice in a dedicated terminal. Then, in your main program, write into "ImageMSVCRequest.txt" the exact name of the image without the extension, followed by a quality setting existing in "Image_MSVC.py" in a [name, quality] format. Example: "Cat, Medium". Valid default qualities are "low", "medium", and "high". Case sensitive only on first letter. Ex: "low" and "Low" are acceptable, "lOw" is an invalid input.

After making a request, up to 200ms may pass before the new image is uploaded to the "Loaded Image" folder. Account for this in your main program with either a sleep function, or a re-read with a timed window to allow some wiggle room. Further updates aim to reduce this to under 100ms.

To load the image, after the delay mentioned above, read the contents of "ImageMSVCResponse.txt" and store it. This is the full filepath of the new file, including name and extension. Use this to load the singular image stored in the "Loaded Image" folder in any way you see fit within your program.

# Troubleshooting
If you receive the error "Invalid input" ensure you followed the input format. Quality requests must match the options in "Image_MSVC.py". At base this is "low", "medium", and "high, first letter being case-sensitive. Ex: "high" or "High" but not "HiGh".

If you receive the error "No image found" ensure you typed the correct name as it must exactly match the image in the "Image Library" folder, minus the extension. Ex: Cat.png must be "Cat". The name may also be typed correctly, but the image was not added to the "Image Library" folder.

Correct formatting for the above would be "Cat, high" or "Cat, High". If you input "Cat.png, high" you may receive a "No image found" error as there is likely no Cat.png.[filetype] in the "Image Library" folder.

# Customization
Quality presets can be added or updated as needed. In resizeByQuality() create your own if-statement followed by your choice of valid string inputs. The downscale variable is multiplied by the height and width, so it can technically be used to add "more" pixels but will not enhance visuals. A downscale value of 1 should be used for your highest preset.

Lines 64-67 are used for the "No image found" error and lines 87-89 are used for the "Invalid input" error. Feel free to change these as needed, but make sure your main program knows what to look for when handling these errors.

If you choose to use differently named folders, edit the directories from lines 10-15 to match your naming scheme. These are referenced by the rest of the program, so no other edits are needed.


# UML Sequence Diagram
<img width="634" height="302" alt="image" src="https://github.com/user-attachments/assets/a9417e84-4246-40e1-925c-4cb0ee0861ec" />
