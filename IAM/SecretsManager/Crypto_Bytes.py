import secrets, random

class Crypto_Bytes():
    key =''


def checkKey(key):
    if key > 0:
        return True

def generateSecret():
    system_random = random.SystemRandom()
    size = system_random.randint(128, 256)
    array = [size]
    length = len(array)
    j =0
    for i in range(length):
        if j == size-1:
            j = 0
        array[j] = system_random.randint(0, 26)
        j = j + 1
    return array