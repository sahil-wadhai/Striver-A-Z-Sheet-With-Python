import math

# if 'i' is prime then all of its multiple are non-prime

def seive_of_erastothenes(N:int)->list[bool]:
    N = N+1
    primes = [True]*(N)  

    for i in range(2,int(math.sqrt(N))+1):
        if primes[i]: # if i is prime
            for j in range(i*2,N,i): # mark multiples of i as not prime
                primes[j] = False
    return primes


# Driver Code
def main():

    #Generate seive of erastothenes
    rangeLeft = 0
    rangeRight = 30
    seive = seive_of_erastothenes(rangeRight)
    for i in range(rangeLeft,rangeRight+1):
        print(i , " " , seive[i])
    


if __name__=="__main__":
    main()