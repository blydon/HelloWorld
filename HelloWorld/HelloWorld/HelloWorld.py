def isprime(n):
    '''Checks for primeness of number.'''
    if n==1:
        return False
    if n == 2 or n==3:
        print n
        return True
    if n % 2 == 0 or n%3==0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    print n
    return True


D = {}
q = 2
while q < 20000:
    if q not in D:
        #yield q
        #isprime(q)
        print q
        D[q * q] = [q]
    else:
        for p in D[q]:
            D.setdefault(p + q, []).append(p)
        del D[q]
    q += 1
