import math

"""
Exculding 1 , lowest factor of any composite number is a prime number

36/2 => 18/2 => 9/3 => 3/3 
Therefore prime factors are [2,2,3,3]

Brute Force : 

n = 36
ans = []
for i in range( 2 , n+1 ):
    while n%i==0:
        ans.append(i)
        n = n//i

"""

def prime_factors(n:int)->list[int] :
    ans = []
    for i in range( 2 , int(math.sqrt(n)) + 1 ):
        while n%i==0:
            ans.append(i)
            n = n//i
    
    # if n is not 1 that means a number or factor is remainning
    # that remaining number is a prime number , so include it to ans
    if(n>1): 
        ans.append(n)

    return ans


# Driver Code
def main():
    # Prime Factorization of n
    n = 49
    print(prime_factors(n))


if __name__=="__main__":
    main()