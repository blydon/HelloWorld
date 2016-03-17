import sys, math

#def isprime(n):
#    '''Checks for primeness of number.'''
#    if n==1:
#        return False
#    if n == 2 or n==3:
#        print n
#        return True
#    if n % 2 == 0 or n%3==0:
#        return False
#    max = n**0.5+1
#    i = 3
#    while i <= max:
#        if n % i == 0:
#            return False
#        i+=2
#    print n
#    return True

def main():

    BigNumber = 7123021421849787414791
    #BigNumber = 71230214218497874147
    SqrtBN = (math.trunc(BigNumber**0.5/10)+1)*10
    print BigNumber
    print SqrtBN

    x1 = SqrtBN - 1
    x3 = SqrtBN - 3
    x7 = SqrtBN - 7
    x9 = SqrtBN - 9

    while x9  > 26400983800:
        if BigNumber%x1 == 0:   
            print str(x1) + " " + str(BigNumber%x1)
        elif BigNumber%x3 == 0:
            print str(x3) + " " + str(BigNumber%x3)
        elif BigNumber%x7 == 0:
            print str(x7) + " " + str(BigNumber%x7)
        elif BigNumber%x9:
            print str(x9) + " " + str(BigNumber%x9)

        x1 -= 10
        x3 -= 10
        x7 -= 10
        x9 -= 10

    print 'End'

    #D = {}
    #q = 2
    #while q < 20000:
    #    if q not in D and isprime(q):            
    #        print q
    #        D[q * q] = [q]
    #    else:
    #        for p in D[q]:
    #            D.setdefault(p + q, []).append(p)
    #        del D[q]
    #    q += 1

if __name__ == "__main__":
    sys.exit(int(main() or 0))


