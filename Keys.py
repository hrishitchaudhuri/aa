import rsa

def keygen():
    '''
        Generates Public and Private keys using the rsa module and
        writes them into key files
    '''
    pkey, pvkey=rsa.newkeys(1024)
    with open('./keys/pub.pem','wb') as pk:
        pk.write(pkey.save_pkcs1('PEM'))
    with open('./keys/pvk.pem','wb') as pvk:
        pvk.write(pvkey.save_pkcs1('PEM'))
    pk.close()
    pvk.close()

def load_keys():
    '''
        loads keys from pvk.pem and pub.pem files into variables and
        return them
    '''
    with open('./keys/pub.pem','r') as f:
        pvkey=rsa.PublicKey.load_pkcs1(f.read())
    
    with open('./keys/pvk.pem','r') as f:
        pkey=rsa.PrivateKey.load_pkcs1(f.read())
    
    return pkey, pvkey
