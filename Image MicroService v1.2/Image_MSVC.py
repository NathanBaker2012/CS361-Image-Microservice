import os
from pathlib import Path
from PIL import Image

main_directory = "FILEPATH"

image_library = main_directory + "\\Image Library"
image_msvc_request = main_directory + "\\ImageMSVCRequest.txt"
image_msvc_response = main_directory + "\\ImageMSVCResponse.txt"
loaded_image_folder = main_directory + "\\Loaded Image"

#Preset downscale values based on quality inputs
def getDownscale(quality):
    if quality == "High" or quality == "high":
        return 1.0
    elif quality == "Medium" or quality == "medium":
        return 0.7
    elif quality == "Low" or quality == "low":
        return 0.4

#Resizes copied image for loading
def resizeByQuality(file, quality, original_image_location):
    img_location = loaded_image_folder + "\\" + file
    image = Image.open(original_image_location)
    downscale = getDownscale(quality)
    width = int(image.width*downscale)
    height = int(image.height*downscale)

    resolution = (width, height)
    new_image = image.resize(resolution, Image.LANCZOS)
    new_image.save(img_location)

#Modify a copy of the original image into loaded_image_folder
def loadNewImage(file, quality):
    for image in os.listdir(loaded_image_folder):
        os.remove(loaded_image_folder + "\\" + image)
    with open(image_msvc_response, "w") as f:
        path = os.path.join(loaded_image_folder, file)
        f.write(path)
        f.close
    original_image_location = image_library + "\\" + file
    resizeByQuality(file, quality, original_image_location)

#Find requested image, make call to load modified image
def sendImage(image_found, image_name, quality):
        for file in os.listdir(image_library):
            filename = Path(image_library + "\\" + file).stem
            if filename == image_name:
                image_found = True
                loadNewImage(file, quality)
        if image_found == False:
             with open(image_msvc_response, "w") as f:
                    f.write("No image found")
                    f.close

#Try loading new image from request
def formatNewImage():
    image_found = False
    try:
        image_name, quality = text_list[0], text_list[1]
        sendImage(image_found, image_name, quality)
    except:
        with open(image_msvc_response, "w") as f:
            f.write("Invalid input")
            f.close

def clearRequest():
    with open(image_msvc_request, "w") as f:
        f.write("")
        f.close
    formatNewImage()
    

#Listens for new text in ImageMSCV.txt
while True:
    image_found = False
    with open(image_msvc_request) as f:
            all_text = f.read()
            text_list = all_text.split(", ")
            f.close()
    if all_text:
        clearRequest()