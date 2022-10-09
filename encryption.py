from img_converter import immagine_ascii
import functions

def crypt(stringa, ascii_img_obj):

    # Trasformo l'array di caratteri ascii in un array di numeri decimali
    decoded_array = functions.from_ascii_to_dec_array(stringa)
    # Array in cui ci saranno i caratteri cryptati
    coded_array = []
    # Qui inizia l algoritmo di codifica
    count1 = 0
    count2 = 0
    for num in decoded_array:
        temp_num = (int)((ascii_img_obj.tot_pixel/ascii_img_obj.caratteri[count1][1])*count2)
        coded_array.append(functions.somma_dec(num, temp_num))
        # Incremento i counter e se il primo supera il numero di caratteri unici nell immagine ascii lo riporto a 0
        count1 = count1 + 1
        count2 = count2 + 1
        if count1 > 10:
            count1 = 0
    coded_ascii_array = functions.from_dec_to_ascii(coded_array)
    coded_string = "".join(coded_ascii_array)
    coded_hex_string = coded_string.encode('utf-8').hex()
    return coded_hex_string


def decrypt(coded_hex_string, ascii_img_obj):

    coded_string = bytes.fromhex(coded_hex_string).decode('utf-8')
    dec_array = functions.from_ascii_to_dec_array(coded_string)
    # Array in cui ci saranno i caratteri decryptati
    decoded_array = []
    # Qui inizia l algoritmo di decodifica
    count1 = 0
    count2 = 0
    for num in dec_array:
        temp_num = (int)((ascii_img_obj.tot_pixel/ascii_img_obj.caratteri[count1][1])*count2)
        decoded_array.append(functions.sottrai_dec(num, temp_num))
        # Incremento i counter e se il primo supera il numero di caratteri unici nell immagine ascii lo riporto a 0
        count1 = count1 + 1
        count2 = count2 + 1
        if count1 > 10:
            count1 = 0
    return "".join(functions.from_dec_to_ascii(decoded_array))

