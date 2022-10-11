from img_converter import immagine_ascii
import img_converter as ic
import functions

def crypt(stringa, ascii_img_obj):

    # Trasformo l'array di caratteri ascii in un array di numeri decimali
    decoded_array = functions.from_ascii_to_dec_array(stringa)
    # Array in cui ci saranno i caratteri cryptati
    coded_array = []
    # Rimuovo dall oggetto dell immagine le posizioni dell array dove il numero di caratteri è 0
    zero_char = []
    for char in ascii_img_obj.caratteri:
        if char[1] == 0:
            zero_char.append(char)
    for char in zero_char:
        ascii_img_obj.caratteri.remove(char)

    # Qui inizia l algoritmo di codifica
    count = 0
    for num in decoded_array:
        temp_num = (int)((ascii_img_obj.tot_pixel/ascii_img_obj.caratteri[count % len(ascii_img_obj.caratteri)][1])*(count + 1))
        coded_array.append(functions.somma_dec(num, temp_num))
        count = count + 1
    coded_ascii_array = functions.from_dec_to_ascii(coded_array)
    coded_string = "".join(coded_ascii_array)
    coded_hex_string = coded_string.encode('utf-8').hex()
    return coded_hex_string


def decrypt(coded_hex_string, ascii_img_obj):

    coded_string = bytes.fromhex(coded_hex_string).decode('utf-8')
    dec_array = functions.from_ascii_to_dec_array(coded_string)
    # Array in cui ci saranno i caratteri decryptati
    decoded_array = []
    # Rimuovo dall oggetto dell immagine le posizioni dell array dove il numero di caratteri è 0
    zero_char = []
    for char in ascii_img_obj.caratteri:
        if char[1] == 0:
            zero_char.append(char)
    for char in zero_char:
        ascii_img_obj.caratteri.remove(char)
    # Qui inizia l algoritmo di decodifica
    count = 0
    for num in dec_array:
        temp_num = (int)((ascii_img_obj.tot_pixel/ascii_img_obj.caratteri[count % len(ascii_img_obj.caratteri)][1])*(count + 1))
        decoded_array.append(functions.sottrai_dec(num, temp_num))
        # Incremento i counter e se il primo supera il numero di caratteri unici nell immagine ascii lo riporto a 0
        count = count + 1
    return "".join(functions.from_dec_to_ascii(decoded_array))
