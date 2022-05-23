import secrets, random
from operator import xor



def generateSecret():
    secretsGenerator = secrets.SystemRandom()
    array = [0] * 128
    index =0
    for i in range(len(array)):
        array[index] = int(secretsGenerator.randint(0, 26))
        index+=1
    return array

def generateUserId():
    userId = secrets.token_hex(64) 
    return userId 


def generateAgentId():
    agentId = secrets.token_hex(64) 
    return agentId 



def encryptOrDecrypt(keys,text):

    arrayByte = bytearray()
    j = 0
    max = len(keys)

    for i in text.encode():

        if(j == max):
            j = 0
        a = hex(i)
        b = hex (keys[j])
        out =  xor(int(a,16),int(b,16))
        arrayByte.append(out)
        j = j + 1
        
    return arrayByte


def decryptDbConnection(text):

    key = [2,23,1,5,26,4,4,6,3,6,25,20,8,9,12,17,13,5,7,2,18,1,21,22,23,12,27,14,20,18,4,8,5,12,16,13,18,23,1,5,3,7,2,12,20,23,25,1,4,6,13,15] 
    de = ""
    dbn = encryptOrDecrypt(key,text)



    for i in dbn:
        de += str(chr(i))
    
    return de
    
