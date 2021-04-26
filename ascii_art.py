def open_letter(caracter):
    """takes a str caracter and returns an array with all the characters to create the letter in ascii art"""
    open_file = open(("alphabet.txt"), "r")
    read_file = open_file.read()
    alphabet = list(read_file.split(","))
    sorti = list(alphabet[corespondance[caracter]].split('\n'))
    return sorti


def write(message):
    """Takes a string and returns this in ascii art"""
    epelle = list(message)
    mot = 0
    temp_mot = 0
    if mot == 0:
        mot = open_letter(epelle[0])
    for letter in range(len(epelle) - 1):
        for lignes in mot:
            temp_mot = open_letter(epelle[letter + 1])
            mot[mot.index(lignes)] = " ".join((lignes, temp_mot[mot.index(lignes)]))
    affiche(mot)


def affiche(message):
    """print the argument"""
    for i in message:
        print(i)



corespondance = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':10,
    'L':11,
    'M':12,
    ',':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25,
    ' ':26,
    'a':27,
    'b':28,
    'c':29,
    'd':30,
    'e':31,
    'f':32,
    'g':33,
    'h':34,
    'i':35,
    'j':36,
    'k':37,
    'l':38,
    'm':39,
    'n':40,
    'o':41,
    'p':42,
    'q':43,
    'r':44,
    's':45,
    't':46,
    'u':47,
    'v':48,
    'w':49,
    'x':50,
    'y':51,
    'z':52,
    '-':53,
    '_':54,
    '0':55,
    '1':56,
    '2':57,
    '3':58,
    '4':59,
    '5':60,
    '6':61,
    '7':62,
    '8':63,
    '9':64,
    ',':65,
    '.':66,
}
