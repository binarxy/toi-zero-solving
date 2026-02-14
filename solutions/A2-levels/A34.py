n = int(input())

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False

    return True

primes = []

for p in range(2,n+1):
    if isPrime(p):
        primes.append(p)

if n in primes:
    print('Yes')
    print(' '.join(map(str,primes)))
else:
    print('No')
