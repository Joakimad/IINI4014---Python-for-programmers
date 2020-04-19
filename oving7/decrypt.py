from oving7.rsa import decrypt


def decrypt_with_publickey(publickey, encrypted_msg, start, end):
    e, n = publickey
    possible_solutions = []
    counter = 0
    for i in range(start, end):
        if counter == 100:
            print(i)
            counter = 0
        counter += 1
        decrypted_msg = decrypt((i, n), encrypted_msg)
        if decrypted_msg.startswith('h'):
            print(decrypted_msg)
            possible_solutions.append((i, decrypted_msg))
    return possible_solutions


def PrimeGen(n=10000):
    primes = []
    chk = 2
    while len(primes) < n:
        ptest = [chk for i in range(2, chk) if chk % i == 0]
        primes += [] if ptest else [chk]
        chk += 1
    return primes


encrypted_msg = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186,
                 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744,
                 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174,
                 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706,
                 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]

publickey = (29815, 100127)

print(decrypt_with_publickey(publickey, encrypted_msg, 64300, 64400))
