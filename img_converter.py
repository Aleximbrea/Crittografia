from turtle import width
from PIL import Image

class immagine_ascii:

    larghezza = None
    altezza = None
    caratteri = [["@", 0],["#", 0],["S", 0],["%", 0],["?", 0],["*", 0],["+", 0],[";", 0],[":", 0],[",", 0],[".", 0]]
    immagine = ""
    tot_pixel = None

    def __init__(self, larghezza, altezza, caratteri, immagine):
        self.larghezza = larghezza
        self.altezza = altezza
        self.caratteri = caratteri
        self.immagine = immagine
        self.tot_pixel = altezza*larghezza
        


def img_to_ascii(immagine, larg):
    
    # Caratteri con la quale verrà disegnata l'immagine
    # I caratteri sono messi in ordine dal più "scuro" al meno "scuro"
    chars = ["@","#","S","%","?","*","+",";",":",",","."]

    # Apriamo l'immagine
    img = Image.open(immagine)

    #Rimpicciolisco l'immagine
    larghezza, altezza = img.size
    ratio = altezza/larghezza
    # Nuove dimensioni
    larghezza = int(larg)
    altezza = int(ratio * larghezza * 0.60)
    img = img.resize((larghezza, altezza))

    # Rendo l'immagine più grigia
    img = img.convert('L')

    # Prendo informazioni sulla luminosità di ogni pixel
    pixels = img.getdata()

    # Vado a sostituire i pixel secondo una scala di luminosità
    pixel_convertiti = [chars[pixel//25] for pixel in pixels]
    pixel_convertiti = "".join(pixel_convertiti)

    # Metto in ordine i pixel 
    # new_pixels_count = len(pixel_convertiti)
    # ascii_image = [pixel_convertiti[index:index + larghezza] for index in range(0, new_pixels_count, larghezza)]
    # ascii_image = "\n".join(ascii_image)

    # Creo l'oggetto dell'immagine
    # Prima creo l'array di tutti i caratteri e il numero di quante volte il carattere è scritto
    char_array = [["@", 0],["#", 0],["S", 0],["%", 0],["?", 0],["*", 0],["+", 0],[";", 0],[":", 0],[",", 0],[".", 0]]
    for char in pixel_convertiti:
        for i in char_array:
            if i[0] == char:
                i[1] = i[1] + 1
    # Ora passo tutti i dati all'oggetto
    img_obj = immagine_ascii(larghezza, altezza, char_array, pixel_convertiti)

    # Ritorno l'oggetto
    return img_obj




