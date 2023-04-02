import requests  
from PIL import Image    
from PIL.ExifTags import TAGS 
import logging   
import sys       
logging.basicConfig(level=logging.DEBUG)


def extract_metadata(image):
    data = {}
    # extracting the exif metadata
    exifdata = image.getexif()

    # extract all tags in getexif
    for tagid in exifdata:

        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)

        # passing the tagid to get its respective value
        value = exifdata.get(tagid)
        # Appending to a dictionnary 
        data[f"{tagname}"] = value

    return data



if __name__ == "__main__":

    url = sys.argv[1]
    response = requests.get(url, stream=True)
    img = Image.open(response.raw)
    output = extract_metadata(img)
    print("METADATA : ", output)

    
