"""package permettant l'écriture de chaine de caractères en ascii art"""


def open_letter(lettre):
    """demande une lettre en str et renvoie dans une liste le caractère en ascii art"""
    open_file = open(("alphabet.txt"), "r")
    read_file = open_file.read()
    alphabet = list(read_file.split(","))
    sorti = list(alphabet[corespondance[lettre]].split('\n'))
    return sorti


def write(message):
    """prend une chaine de caractères et la print en ascii art"""
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
    """affiche une lettre ascii art à partir d'une liste"""
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

write('3.14')