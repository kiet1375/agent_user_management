import secrets, random

class Crypto_Bytes():
    key =''


def checkKey(key):
    if key > 0:
        return True

def generateSecret():
    secretsGenerator = secrets.SystemRandom()
    size = int(secretsGenerator.randint(128, 256))
    array = [256]
    j =0
    for i in range(256):
        array[j] = int(secretsGenerator.randint(0, 26))

    return array