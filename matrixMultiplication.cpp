
int** conv(int** A, int** B) {
    int n = A[0].length();
    int R[n][n];
    for (int i = 0; i < n) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                R[i][j] += A[j][k] * B[k][j];
            }
        }
    }
    return R;
}

int** matrixSectionner(int** A, int adderLine, int adderColon) {
    int n = A[0].length();
    int R[n/2][n/2];
    for (int i = 0; i < n/2; i++) {
        for (int j = 0; j < n/2; j++) {
            R[i][j] = A[i + adderLine][j + adderColon];
        }
    }
    return R;
}

int** matrixConcatenater(int** A11, int** A12, int** A21, int** A22) {
    int n = 2 * A11[0].length();
    int R[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i < n/2 && j < n/2) {
                R[i][j] = A11[i][j];
            } else if (i < n/2 && j > n/2) {
                R[i][j] = A12[i][j];
            } else if (i > n/2 && j < n/2) {
                R[i][j] = A21[i][j];
            } else {
                R[i][j] = A22[i][j];
            }
        }
    }
    return R;
}

int** matrixAdditionner(int** A, int** B) {
    int n = A[0].length();
    int R[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            R[i][j] = A[i][j] + B[i][j];
        }
    }
    return R;
}

int** matrixSoustracter(int** A, int** B) {
    int n = A[0].length();
    int R[n][n];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            R[i][j] = A[i][j] - B[i][j];
        }
    }
    return R;
}

int** strassen(int** A, int** B) {
    int n = A[0].lenght();
    int R[n][n];

    if (n == 1) {
        R[1][1] = A[1][1] * B[1][1];
    }
    else {

        int A11[n/2][n/2] = matrixSectionner(A, 0, 0);
        int A12[n/2][n/2] = matrixSectionner(A, 0, n/2);
        int A21[n/2][n/2] = matrixSectionner(A, n/2, 0);
        int A22[n/2][n/2] = matrixSectionner(A, n/2, n/2);
        
        int B11[n/2][n/2] = matrixSectionner(B, 0, 0);
        int B12[n/2][n/2] = matrixSectionner(B, 0, n/2);
        int B21[n/2][n/2] = matrixSectionner(B, n/2, 0);
        int B22[n/2][n/2] = matrixSectionner(B, n/2, n/2);

        int M1[n/2][n/2] = strassen(matrixAdditionner(A11, A22), matrixAdditionner(B11, B22));
        int M2[n/2][n/2] = strassen(matrixAdditionner(A21, A22), B11);
        int M3[n/2][n/2] = strassen(A11, matrixSoustracter(B12, B22));
        int M4[n/2][n/2] = strassen(A22, matrixSoustracter(B21, B11));
        int M5[n/2][n/2] = strassen(matrixAdditionner(A11, A12), B22);
        int M6[n/2][n/2] = strassen(matrixSoustracter(A21, A11), matrixAdditionner(B11, B12));
        int M7[n/2][n/2] = strassen(matrixSoustracter(A12, A22), matrixAdditionner(B21, B22));

        int C11[n/2][n/2] = matrixSoustracter(matrixAdditionner(M1, M2), matrixAdditionner(M5, M7)); 
        int C12[n/2][n/2] = matrixAdditionner(M3, M5);
        int C21[n/2][n/2] = matrixAdditionner(M2, M4);
        int C22[n/2][n/2] = matrixaddditionner(matrixSoustracter(M1, M2), matrixAdditionner(M3, M6));

        R = matrixConcatener(C11, C12, C21, C22);
    } 
    return R;
}

int** strassen(int** A, int** B, int seuil) {
    int n = A[0].lenght();
    int R[n][n];

    if (n == seuil) {
        R = conv(A, B);
    }
    else {

        int A11[n/2][n/2] = matrixSectionner(A, 0, 0);
        int A12[n/2][n/2] = matrixSectionner(A, 0, n/2);
        int A21[n/2][n/2] = matrixSectionner(A, n/2, 0);
        int A22[n/2][n/2] = matrixSectionner(A, n/2, n/2);
        
        int B11[n/2][n/2] = matrixSectionner(B, 0, 0);
        int B12[n/2][n/2] = matrixSectionner(B, 0, n/2);
        int B21[n/2][n/2] = matrixSectionner(B, n/2, 0);
        int B22[n/2][n/2] = matrixSectionner(B, n/2, n/2);

        int M1[n/2][n/2] = strassen(matrixAdditionner(A11, A22), matrixAdditionner(B11, B22));
        int M2[n/2][n/2] = strassen(matrixAdditionner(A21, A22), B11);
        int M3[n/2][n/2] = strassen(A11, matrixSoustracter(B12, B22));
        int M4[n/2][n/2] = strassen(A22, matrixSoustracter(B21, B11));
        int M5[n/2][n/2] = strassen(matrixAdditionner(A11, A12), B22);
        int M6[n/2][n/2] = strassen(matrixSoustracter(A21, A11), matrixAdditionner(B11, B12));
        int M7[n/2][n/2] = strassen(matrixSoustracter(A12, A22), matrixAdditionner(B21, B22));

        int C11[n/2][n/2] = matrixSoustracter(matrixAdditionner(M1, M2), matrixAdditionner(M5, M7)); 
        int C12[n/2][n/2] = matrixAdditionner(M3, M5);
        int C21[n/2][n/2] = matrixAdditionner(M2, M4);
        int C22[n/2][n/2] = matrixaddditionner(matrixSoustracter(M1, M2), matrixAdditionner(M3, M6));

        R = matrixConcatener(C11, C12, C21, C22);
    } 
    return R;
}