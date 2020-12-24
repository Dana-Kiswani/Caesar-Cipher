import string
import nltk
nltk.download('words')


def decrypt(string, key):
    return encrypt(string, -key)


def encrypt(string_, key):

    alpha = string.ascii_lowercase
    alphabet_list = list(alpha)
    value = ''
    for character in string_:
        letter = 0
        if not character.isalpha() : 
            if character ==' ' : 
                value += character
            continue
        character=character.lower()
        ind = (alphabet_list.index(character) + key)
        letter += ind
        letter = letter % 26
        value = value + alphabet_list[letter]

    return value


def breack__(string):
    arr_br = []
    for i in range(26):
        decrypted = decrypt(string,i)
        arr_br.append(decrypted)


# [A.B.C.D.E.F.G.H.I.G.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z]
if __name__ == "__main__":
    print( encrypt('here', -4))
    print(decrypt('aktd ahqc', -1))
    print( encrypt('Mfqelk', 3))
