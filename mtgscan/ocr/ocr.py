from mtgscan.box_text import BoxTextList
import easyocr
import pathlib


class OCR:
    def __init__(self):
        self.reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
        

    def image_to_box_texts(self, image: str | pathlib.PosixPath) -> BoxTextList:
        """Apply OCR on an image containing Magic cards

        Parameters
        ----------
        image : str
            URL or path to an image

        Returns
        -------
        BoxTextList
            Texts and boxes recognized by the OCR
        """
        if type(image) is pathlib.PosixPath:
            image = str(image)

        analysis = self.reader.readtext(image, detail = 1)
        box_texts = BoxTextList()
        for line in analysis:
            box_texts.add(line[0], line[1])
        return box_texts
