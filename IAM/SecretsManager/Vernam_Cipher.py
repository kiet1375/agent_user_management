from operator import xor


def encryptOrDecrypt(keys,text):

    arrayByte = bytearray()
    j = 0

    for i in text.encode():

        if(j == len(keys)):
            j = 0
        a = hex(i)
        b = hex (keys[j])
        out =  xor(int(a,16),int(b,16))
        arrayByte.append(out)
        j = j + 1
        
    return arrayByte