#include <iostream>
#include <ifstream>
#include <matrixMultiplication.cpp>

using namespace std;


int** getMatrix(string filename) {
    int** R;
    
    string mLine;
    ifstream readFile(filename);

    int i = 0;
    while(getline(readFile, mLine)) {
        R[i] = strtok(mLine, "\t") 
        i++;
    }
    return R;
}

int main(int argc, char* argv[]) {
    
    int** m;
    int** A = getMatrixx("ex"+argv[0]+"_0");
    int** B = getMatrixx("ex"+argv[0]+"_1");

    if (argv[1] == 0) {
        m = conv(A, B);
    } else if (argv[1] == 1) {
        m = strassen(A, B);
    } else if (argv[1] == 2) {
        m = strassenSeuil(A, B);
    }
    

    return 0;
}