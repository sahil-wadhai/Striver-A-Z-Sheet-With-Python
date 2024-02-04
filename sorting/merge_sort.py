def merge(arr,start,mid,end):
    left = start
    right = mid+1
    temp = []
    while left <= mid and right <= end:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while(left<=mid):
        temp.append(arr[left])
        left += 1
    while(right<=end):
        temp.append(arr[right])
        right += 1
    
    k=0
    for i in range(start,end+1):
        arr[i] = temp[k]
        k+=1


def merge_sort(arr,start,end):
    if start >= end:
        return
    mid = (start+end)//2

    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge(arr,start,mid,end)

def sort(arr):
    n = len(arr)
    merge_sort(arr,0,n-1)

def main():
    arr = [1,7,5,3]
    print("Before Sorting : ",arr)
    sort(arr)
    print("After Sorting : ",arr)

if __name__=="__main__":
    main()