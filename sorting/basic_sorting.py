"""
Bubble Sort :
- stable
- Time Complexity : O(n) , O(n^2) , O(n^2)
- Space Complexity : O(1)

Insertion Sort :
- stable
- Time Complexity : O(n) , O(n^2) , O(n^2)
- Space Complexity : O(1)

Selection Sort :
- not stable
- Time Complexity : O(n^2) , O(n^2) , O(n^2)
- Space Complexity : O(1)

"""


def bubble_sort(arr): 
  print("Bubble Sort : ")
  n = len(arr)
  for i in range(0,n):  
    for j in range(0,n-1-i):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

def insertion_sort(arr):
  print("Insertion Sort : ")
  n = len(arr)
  for i in range(0,n):
    for j in range(i-1,-1,-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

#driver code
def main():
  arr = [4,2,7,5,4,6]
  print("Before Sorting : ",arr,end="\n\n")
  #bubble_sort(arr)
  insertion_sort(arr)
  print("After Sorting : ",arr,end=" ")


if __name__ == "__main__":
  main()