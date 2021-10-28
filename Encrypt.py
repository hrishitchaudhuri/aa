import rsa
import base64

def encrypt(msg, key):
    '''
        Pass byte array (bytes()) as msg and pass a PublicKey object to key
        return a cipher text encrypted by rsa.encrypt
    '''
    cipher=b''
    i=0
    while i<len(msg):
        if i+86>len(msg):
            rem=len(msg)-i+86
            cipher+=rsa.encrypt(base64.b64encode(msg[i:i+rem]),key)
            break
        cipher+=rsa.encrypt(base64.b64encode(msg[i:i+86]),key)
        i+=86
    return cipher