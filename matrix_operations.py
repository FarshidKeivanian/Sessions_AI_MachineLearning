# src/hello.py
def matmul(A, B):
    rows, cols = len(A), len(B[0])
    K = len(B)
    return [[sum(A[r][k]*B[k][c] for k in range(K)) for c in range(cols)] for r in range(rows)]

def det2(M):
    a,b,c,d = M[0][0],M[0][1],M[1][0],M[1][1]
    return a*d - b*c

def det3(M):
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print("A*B =", matmul(A,B))         # [[19, 22], [43, 50]]
print("det(A) =", det2(A))          # -2
C = [[2,0,1],[3,0,0],[5,1,1]]
print("det(C) =", det3(C))          # Expected: -3
