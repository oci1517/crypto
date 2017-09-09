def modular_inverse(e, phi, max_iter=1e6):
    for d in range(max_iter):
        if pow(d, e, phi) == 1:
           return d 


def primes_sieve(limit):
    '''

    Crible d'eratosthène (générateur des nombres premiers inférieurs à
    ``limit``)

    source : http://stackoverflow.com/a/3941967

    '''
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def factor(n):
    ''' retourne les facteurs premiers de n '''
    for p in primes_sieve(int(n ** .5)):
        q = n / p
        if isinstance(q, int):
            return [p, q]
            
    return []
        

def guess_private_key(publicKey):
    m, e = publicKey
    p, q = [5839, 16649]
    phi = (p-1) * (q - 1)
    d = modular_inverse(e, phi, 10 ** 9)

    return [m, d]

publicKey  = [97213511, 6551]
print(guess_private_key(publicKey))

    