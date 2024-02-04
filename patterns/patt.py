def square(n):
  for i in range(0,n):
    for j in range(0,n):
      print("*",end=" ")
    print()
  
def triangle1(n):
  for i in range(0,n):
    for j in range(0,i+1):
      print("*",end=" ")
    print()

def triangle2(n):
  for i in range(0,n):

    for j in range(0,n-i):
      print(" ",end="")

    for j in range(0,i+1):
      print("*",end="")

    for j in range(0,i):
      print("*",end="")
    print()

def triangle3(n):
  for i in range(0,n):

    for j in range(0,n-i):
      print(" ",end="")

    for j in range(0,i+1):
      print(chr(ord('A')+j),end="")

    for j in range(0,i):
      print(chr(ord('A')+i-j-1),end="")
    print()


#driver code
def main():
  square(5)
  print()

  triangle1(6)
  print()

  triangle2(6)
  print()
  
  triangle3(6)

#code entrance point
if __name__=="__main__":
  main()

"""
Output:

* * * * * 
* * * * * 
* * * * * 
* * * * *
* * * * *
*
* *
* * *
* * * *
* * * * *
* * * * * *
      *
     ***
    *****
   *******
  *********
 ***********
      A
     ABA
    ABCBA
   ABCDCBA
  ABCDEDCBA
 ABCDEFEDCBA

"""
