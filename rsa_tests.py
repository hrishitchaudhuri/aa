from RSA import encrypt, keygen

def keytest():
    k = [128, 256, 512, 1024, 2048]
    trials = 100
    try:
        for i in k:
            print(f'------Testing for bitlength {i}------')
            passed1=0
            passed2=0
            msg='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=~`'
            msg2='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
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

            print(f'{i} bits enc/dec passed \nmsg1: {(passed1/trials)*100}% of the time\nfor msg2: {(passed2/trials)*100}% of the time')
                
            
    except OverflowError:
        print(f'overflowed for bitlength {i} at iteration {j}')
        pass

if __name__=='__main__':
    keytest()
