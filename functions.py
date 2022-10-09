
def from_ascii_to_dec_array(stringa):
    
    decimal_array = []
    decimal_string = ""
    for char in stringa:
        decimal_array.append(ord(char))
    return decimal_array


def from_dec_to_ascii(array):
    
    ascii_string = []
    for i in array:
        ascii_string.append(chr(i))
    return ascii_string



def somma_dec(num, addendo):
    coded = False
    num = num + addendo
    while coded is False:
        while num > 126:
            num = num - 126
        while num < 32:
            num = num + addendo
        if num > 31 and num < 127:
            coded = True
    return num


def sottrai_dec(num, sottraendo):
    coded = False
    num = num - sottraendo
    while coded is False:
        while num < 0:
            # Con il - davanti num trasformo un numero negativo in positivo
            num = 126 - -num
        while num > 126:
            num = num - sottraendo
        while num < 32:
            num = num + 126
        if num > 31 and num < 127:
            coded = True
    return num
            


if __name__ == "__main__":
    num = 104
    n = 11000

    a = somma_dec(num, n)
    print(a)
    b = sottrai_dec(a, n)
    print(b)

