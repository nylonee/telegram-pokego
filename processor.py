# image processing dependencies
from PIL import Image, ImageEnhance
import pytesseract

# system dependencies
import ast
import re

class ImageProcessor():
    """make an image OCR-able, and regex the text to file"""
    def __init__(self, f):
        self.f = f
        try:
            open(self.f, 'x') # attempt to create the file
            print("{} didn't exist, created a new file".format(self.f))
        except FileExistsError:
            pass

    def _scan_photo(self, phototext):
        print(phototext)
        # Attempt to use regex to pull useful data from the photo
        hp = self._regex_match(r'HP[ ]?[0-9]{1,4}[ ]?\/[ ]?([0-9]{1,4})', phototext)
        pokemonline = self._regex_match(r'UST ([A-Z]*) CAN', phototext)
        evolve = self._regex_match(r'(EVOLVE)[ ]?.*', phototext)
        evolve_candy = self._regex_match(r'EVOL[\D]{1,10}([\d]{2,3})', phototext)

        print({'hp':hp, 'pokemon':pokemonline, 'evolve':evolve, 'candy':evolve_candy})
        return {'hp':hp, 'pokemon':pokemonline, 'evolve':evolve, 'candy':evolve_candy}

    def _regex_match(self, regex, text):
        match = re.search(regex, text)
        return match.group(1) if match else None

    def _save_photo_data(self, dict_to_save):
        with open(self.f, 'a', encoding='utf-8') as f:
            f.write("{}\n".format(str(dict_to_save)))

    def get_last_line(self):
        """return the last line of photo data stored, for evolve comparison"""
        with open(self.f) as f:
            #find the last line
            last = None
            for last in (line for line in f if line.rstrip('\n')):
                pass

        try:
            return ast.literal_eval(last)
        except ValueError:
            return None

    def _manipulate_photo(self, path):
        """given a photo path, manipulate the photo for better OCR"""
        enh = Image.open(path)

        enh = ImageEnhance.Contrast(enh).enhance(2)
        enh = ImageEnhance.Sharpness(enh).enhance(2)
        #TODO: erode and dilate
        return enh

    def process_photo(self, path, properties):
        """scan a photo and save the data to a file. Return the data saved"""
        phototext = pytesseract.image_to_string(self._manipulate_photo(path))
        pdict = {**self._scan_photo(phototext), **properties}
        self._save_photo_data(pdict)
        return pdict
