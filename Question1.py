M = 3
N = 4
 
def transpose(A, B):
    for i in range(N):
        for j in range(M):
            B[i][j] = A[j][i]
 
A = [ [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]]
 
B = [[0 for x in range(M)] for y in range(N)]
 
transpose(A, B)
print("Result matrix is")
for i in range(N):
    for j in range(M):
        print(B[i][j], "", end='')
    print()  