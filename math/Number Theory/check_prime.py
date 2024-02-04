import math

"""
To check if n is prime
if any i less than n divides n perfectly
then n is not prime 

Brute Force : 

for i in range(2,n):
    if n%i == 0:
        return False
return True

"""

def isPrime(n:int)->bool:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# Driver Code
def main():
    #Check If Prime
    n = 49
    print(n , " is prime ? : ", isPrime(n))

if __name__=="__main__":
    main()