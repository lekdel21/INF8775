
def show(matrix):
    n = len(matrix)
    for i in range(0, n):
        for j in range(0, n):
            print(str(matrix[i][j]) + "\t", end = '')
            if j == n - 1: print("\n")


def conv(A, B):
    n = len(A[0])
    R = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                R[i][j] +=  A[i][k] * B[k][j]

    return R

def sectionner(A, adderLine, adderColon):
    n = int((len(A[0]))/2)
    R = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            R[i][j] = A[i + adderLine][j + adderColon]
    return R

def concatenater(A11, A12, A21, A22):
    n = (len(A11[0]))
    R = [[0 for _ in range(n*2)] for _ in range(n*2)]

    for i in range(n*2):
        for j in range(n*2):
            if (i < n) and (j < n): R[i][j] = A11[i][j]
            elif (i < n) and (j >= n): R[i][j] = A12[i][j-n]
            elif (i >= n) and (j < n): R[i][j] = A21[i-n][j]
            elif (i >= n) and (j >= n): R[i][j] = A22[i-n][j-n]
    return R


def substractor(A, B):
    n = len(A[0])
    R = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j] - B[i][j]

    return R

def adder(A, B):
    n = len(A[0])
    R = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            R[i][j] = A[i][j] + B[i][j]

    return R


def strassen(A, B):
    n = len(A[0])
    R = [[0 for _ in range(n)] for _ in range(n)]

    if n == 1: 
        R[0][0] = A[0][0] * B[0][0]
        return R
    
    k = int((len(A[0]))/2)
    A11 = [[0 for _ in range(k)] for _ in range(k)]
    A12 = [[0 for _ in range(k)] for _ in range(k)]
    A21 = [[0 for _ in range(k)] for _ in range(k)]
    A22 = [[0 for _ in range(k)] for _ in range(k)]
    
    B11 = [[0 for _ in range(k)] for _ in range(k)]
    B12 = [[0 for _ in range(k)] for _ in range(k)]
    B21 = [[0 for _ in range(k)] for _ in range(k)]
    B22 = [[0 for _ in range(k)] for _ in range(k)]

    
    for i in range(0, k):
        for j in range(0, k):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + k]
            A21[i][j] = A[i + k][j]
            A22[i][j] = A[i + k][j + k]
            
            B11[i][j] = B[i][j]
            B12[i][j] = B[i][j + k]
            B21[i][j] = B[i + k][j]
            B22[i][j] = B[i + k][j + k]

    P5 = strassen(adder(A11, A22), adder(B11, B22))         #P5
    P3 = strassen(adder(A21, A22), B11)                     #P3
    P1 = strassen(A11, substractor(B12, B22))               #P1
    P4 = strassen(A22, substractor(B21, B11))               #P4
    P2 = strassen(adder(A11, A12), B22)                     #P2
    P7 = strassen(substractor(A11, A21), adder(B11, B12))   #P7
    P6 = strassen(substractor(A12, A22), adder(B21, B22))   #P6

    C11 = adder(substractor(adder(P5, P4), P2), P6)
    C12 = adder(P1, P2)
    C21 = adder(P3, P4)
    C22 = substractor(substractor(adder(P5, P1), P3), P7)

    return concatenater(C11, C12, C21, C22)

def strassenSeuil(A, B, seuil):
    n = len(A[0])
    R = [[0 for _ in range(n)] for _ in range(n)]
    
    if n <= seuil: 
        R = conv(A, B)
        return R

    k = int((len(A[0]))/2)
    A11 = [[0 for _ in range(k)] for _ in range(k)]
    A12 = [[0 for _ in range(k)] for _ in range(k)]
    A21 = [[0 for _ in range(k)] for _ in range(k)]
    A22 = [[0 for _ in range(k)] for _ in range(k)]
    
    B11 = [[0 for _ in range(k)] for _ in range(k)]
    B12 = [[0 for _ in range(k)] for _ in range(k)]
    B21 = [[0 for _ in range(k)] for _ in range(k)]
    B22 = [[0 for _ in range(k)] for _ in range(k)]

    
    for i in range(0, k):
        for j in range(0, k):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + k]
            A21[i][j] = A[i + k][j]
            A22[i][j] = A[i + k][j + k]
            
            B11[i][j] = B[i][j]
            B12[i][j] = B[i][j + k]
            B21[i][j] = B[i + k][j]
            B22[i][j] = B[i + k][j + k]

    P5 = strassen(adder(A11, A22), adder(B11, B22))         #P5
    P3 = strassen(adder(A21, A22), B11)                     #P3
    P1 = strassen(A11, substractor(B12, B22))               #P1
    P4 = strassen(A22, substractor(B21, B11))               #P4
    P2 = strassen(adder(A11, A12), B22)                     #P2
    P7 = strassen(substractor(A11, A21), adder(B11, B12))   #P7
    P6 = strassen(substractor(A12, A22), adder(B21, B22))   #P6

    C11 = adder(substractor(adder(P5, P4), P2), P6)
    C12 = adder(P1, P2)
    C21 = adder(P3, P4)
    C22 = substractor(substractor(adder(P5, P1), P3), P7)

    return concatenater(C11, C12, C21, C22)