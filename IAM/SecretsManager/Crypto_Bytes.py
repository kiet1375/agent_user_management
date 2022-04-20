import secrets, random

class Crypto_Bytes():
    key =''


def checkKey(key):
    if key > 0:
        return True

def generateSecret():
    secretsGenerator = secrets.SystemRandom()
    array = [0] * 256
    index =0
    for i in range(len(array)):
        array[index] = int(secretsGenerator.randint(0, 26))
        index+=1
    return array