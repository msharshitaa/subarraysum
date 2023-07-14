def subarraysum(A):
    result=0
    for i in range(len(A)):
        sum=0
        for j in range(i,len(A)):
            sum+=A[j]
            result+=sum
    return result
A=list(map(int,input().split()))
print(subarraysum(A))
