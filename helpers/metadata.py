from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(path: str):
    image = Image.open(path)
    exif_data = image.getexif()
    return dict(exif_data)

# print(get_exif("/home/devve/Pictures/Camera/IMG_20201122_012956.jpg"))