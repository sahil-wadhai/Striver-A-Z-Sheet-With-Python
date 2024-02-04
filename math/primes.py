import math

def isPrime(n:int)->bool:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


def seive_of_erastothenes(N:int)->list[bool]:
    N = N+1
    primes = [True]*(N)  

    for i in range(2,N//2):
        if primes[i]:
            for j in range(i*2,N,i):
                primes[j] = False
    return primes

def prime_factors(n:int)->list[int] :
    ans = []
    for i in range( 2 , int(math.sqrt(n))+1 ):
        while n%i==0:
            ans.append(i)
            n = n//i
    
    if(n>1): ans.append(n)

    return ans


# Driver Code
def main():
    #Check If Prime
    n = 49
    print(n , " is prime ? : ", isPrime(n))

    #Generate seive of erastothenes
    rangeLeft = 0
    rangeRight = 30
    seive = seive_of_erastothenes(rangeRight)
    for i in range(rangeLeft,rangeRight+1):
        print(i , " " , seive[i])
    
    print(prime_factors(10))


if __name__=="__main__":
    main()