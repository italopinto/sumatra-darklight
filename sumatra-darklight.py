__author__ = 'Italo Pinto <italosp00@gmail.com>'

SUMATRA_SETTINGS_PATH = r'C:\Users\<user_name>\path\to\SumatraPDF\SumatraPDF-settings.txt'

WHITE = '#ffffff'
BLACK = '#000000'
KEY_1 = 'TextColor'
KEY_2 = 'BackgroundColor'
K1_INDEX = 10
K2_INDEX = 11

text = []
text2 = []
text3 = []

def black(index:int, txt:list, key:str) -> list:
    """Modifies the specified `key` to black value"""
    txt.pop(index)
    txt.insert(index, f'\t{key} = {BLACK}\n')
    return txt


def white(index:int, txt:list, key:str) -> list:
    """Modifies the specified `key` to white value"""
    txt.pop(index)
    txt.insert(index, f'\t{key} = {WHITE}\n')
    return txt


def txt_write(txt:list, file):
    """Receives the list of lines to write in to received file"""
    for line in txt:
        file.write(line)


with open(SUMATRA_SETTINGS_PATH) as smt:
    for x in smt:
        text.append(x)

with open(SUMATRA_SETTINGS_PATH, 'w') as smt:
    for line in text:

        if KEY_1 in line:
            if BLACK in line:
                text2 = white(K1_INDEX, text, KEY_1)
            elif WHITE in line:
                text2 = black(K1_INDEX, text, KEY_1)

        if KEY_2 in line:
            if WHITE in line:
                text3 = black(K2_INDEX, text2, KEY_2)
                txt_write(text3, smt)
                break
            elif BLACK in line:
                text3 = white(K2_INDEX, text2, KEY_2)
                txt_write(text3, smt)
                break



