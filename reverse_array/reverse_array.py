def reverse_array(A):
    start=0
    end=len(A)-1
    for i in range(len(A)//2):
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
    return A


A=list(map(int,input("Enter the array Elements: ").split()))
output=reverse_array(A)
print("Reversed Array: ")
for i in range(len(A)):
    print(A[i],end=" ")