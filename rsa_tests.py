from RSA import encrypt, keygen
import rsa

def keytest():
    k = [32, 64, 128, 256, 512, 1024, 2048]
    trials = 100
    try:
        for i in k:
            print(f'------Testing for bitlength {i}------')
            passed1=0
            passed2=0
            msg='01234'
            msg2='!@#$%'
            # msg='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=~`'
            # msg2='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            for j in range(trials):
                keys=keygen(i)

                c1=encrypt(msg.encode('utf-8'),keys['public'][0],keys['public'][1], keysize=i)
                d1=encrypt(c1,keys['private'][0], keys['private'][1], keysize=i)

                c2=encrypt(msg2.encode('utf-8'),keys['public'][0],keys['public'][1], keysize=i)
                d2=encrypt(c2,keys['private'][0], keys['private'][1], keysize=i)

                if d1==msg.encode('utf-8'):
                    passed1 += 1
                if d2==msg2.encode('utf-8'):
                    passed2 += 1

            print(f'{i} bits enc/dec passed \nmsg1: {(passed1/trials)*100}% of the time\nmsg2: {(passed2/trials)*100}% of the time')
                
            
    except OverflowError:
        print(f'overflowed for bitlength {i} at iteration {j}')
        pass

def module_test():
    k = [32, 64, 128, 256, 512, 1024, 2048]
    trials = 100
    # msg1='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # msg2='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=~`'
    msg1 = '01235'
    msg2 = '!@#$*'
    for i in k:
        p1, p2 = 0, 0
        rp1, rp2 = 0, 0
        print(f'------Testing for {i} bits------')
        for j in range(trials):
            pub, priv = rsa.newkeys(nbits=i)
            keys = keygen(i)

            rc1 = rsa.encrypt(msg1.encode('utf-8'),pub)
            rd1 = rsa.decrypt(rc1, priv)
            c1=encrypt(msg1.encode('utf-8'),keys['public'][0],keys['public'][1], keysize=i)
            d1=encrypt(c1,keys['private'][0], keys['private'][1], keysize=i)
            
            rc2 = rsa.encrypt(msg2.encode('utf-8'),pub)
            rd2 = rsa.decrypt(rc2,priv)
            c2=encrypt(msg2.encode('utf-8'),keys['public'][0],keys['public'][1], keysize=i)
            d2=encrypt(c2,keys['private'][0], keys['private'][1], keysize=i)

            if d1==msg1.encode('utf-8'):
                p1+=1
            if d2==msg2.encode('utf-8'):
                p2+=1
            if rd1==msg1.encode('utf-8'):
                rp1+=1
            if rd2==msg2.encode('utf-8'):
                rp2+=1
        print(f'rsa:\nmsg1: passed {rp1}%\nmsg2: passed {rp2}%')
        print(f'imp:\nmsg1: passed {p1}%\nmsg2: passed {p2}%')


if __name__=='__main__':
    keytest()
    #module_test()