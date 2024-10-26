import sys
def count(arr):
    result=[]
    n=len(arr)
    if n==0:
        return 0
    for i in range(n):
        left_flag=True
        for j in range(i):
            if arr[j]>=arr[i]:
                left_flag=False
                break
        right_flag=True
        for k in range(i+1,n):
            if arr[k]<=arr[i]:
                right_flag=False
                break
        if left_flag and right_flag:
            result.append(arr[i])
    return result
# data=sys.stdin.read()
# lines=data.strip().split('\n')
arr=[1,3,2,4,5]
print(count(arr))
 
        