import secrets, random

def generateSecret():
    secretsGenerator = secrets.SystemRandom()
    array = [0] * 256
    index =0
    for i in range(len(array)):
        array[index] = int(secretsGenerator.randint(0, 26))
        index+=1
    return array