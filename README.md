# CS361-Image-Microservice

This microservice uses "ImageMSVCRequest.txt" as a pipeline to request, by name, an image from the "Image Library" folder be saved into the "Loaded Image" folder with updated quality settings, then uses "ImageMSVCResponse.txt" as a pipeline to respond with the full path of that file for the requesting program to use.

# Setup
In your IDE terminal install with the following (designed for Python 3+):

pip install os-sys

pip install pathlib

pip install Pillow

1. Download the "Image Microservice" zip file and extract the "Image Microservice v[x.x]" folder wherever you like within your project. This microservice can be used anywhere, but be sure to only extract it where other files/projects are not finicky about folder contents. Ideally this will be the root of your main project, or in parallel with the folder holding your main project.

2. Open Image_MSVC.py and update "FILEPATH" in the "main_directory" variable to the root of the "Image Microservice" folder (include the "Image Microservice" folder). Ensure slash formatting matches document, as of now this means using double backslashes \ \ between folders.

3. In "Image Library" add all your high fidelity images. It is recommended to use a simple, but consistent and clear naming scheme.

# How to Request an Image

1. Run the Image Microservice in a dedicated terminal
2. Create a variable to hold the name of the image you wish to request, as a string
```
#Example variable assignment
image_name = "Cat"
```
4. Create a variable to hold the quality setting you wish to request, as a string
```
#Example variable assignment
quality = "Medium"
```
6. In your main program, write the exact name of the image you want and the quality without the file extension into the "ImageMSVCRequest.txt". (Ex: "[IMAGENAME], [QUALITY]")
```
#Example request in Python, exchange "FILEPATH" for the path you used in the Setup above.
main_directory = "FILEPATH"

image_msvc_request = main_directory + "\\ImageMSVCRequest.txt"
image_msvc_response = main_directory + "\\ImageMSVCResponse.txt"

image_name = "Cat"
quality = "Medium"

with open(image_msvc_request, "w") as f:
        request = image_name + ", " + quality
        f.write(request)
        f.close
```

Notes:
- Valid default qualities are "low", "medium", and "high". Case sensitive only on first letter. Ex: "low" and "Low" are acceptable, "lOw" is an invalid input.
- After making a request, up to 200ms may pass before the new image is uploaded to the "Loaded Image" folder. Account for this in your main program with either a sleep function, or a re-read with a timed window to allow some wiggle room. Further updates aim to reduce this to under 100ms.

# How to Receive an Image

1. Make sure the 200ms delay mentioned previously is adhered to, then read the contents of "ImageMSVCRESPONSE.txt" and store it in a variable.
```
#Wait 200ms, then open and save response.
    time.sleep(0.2)
    with open(image_msvc_response) as f:
        image_MSVC_response = f.read()
        f.close()
```
3. Pull the image from the filepath and resize as needed. How you open or store this image is entirely up to you.
```
if image_MSVC_response == "No image found":
        print("Error: No image found")    
    elif image_MSVC_response == "Invalid input":
        print("Error: Invalid input")
    elif image_MSVC_response:
        image_path = image_MSVC_response
        raw_image = Image.open(image_path)
        resized_image = raw_image.resize((120, 150), Image.LANCZOS)
   #Below is an example of using Tkinter to resize or display such an image. Your implementation may differ.
        character_image = ImageTk.PhotoImage(resized_image)
        char_img_label = tk.Label(root, image=character_image)
        char_img_label.image = character_image
        char_img_label.grid(row=9, column=0)
```

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
