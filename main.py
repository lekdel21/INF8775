import sys
import matrix
import time

def main():   
    
    algorithm = sys.argv[1]
    matrixFile1 = sys.argv[2]
    matrixFile2 = sys.argv[3]
    option1 = ""
    option2 = ""

    if len(sys.argv) > 4:
        option1 = sys.argv[4]
    if len(sys.argv) > 5:
        option2 = sys.argv[5]

    with open(matrixFile1, 'r') as f:
        m1 = [[int(num) for num in line.split(' ')] for line in f]
    m1.pop(0)
    with open(matrixFile2, 'r') as f:
        m2 = [[int(num) for num in line.split(' ')] for line in f]
    m2.pop(0)

    start = time.time()

    if algorithm == "conv":
        R = matrix.conv(m1, m2)
        end = time.time()
    
    elif algorithm == "strassen":
        R = matrix.strassen(m1, m2)
        end = time.time()

    elif algorithm == "strassenSeuil":
        R = matrix.strassenSeuil(m1, m2, 10)
        end = time.time()

    
    if option1 == "show" or option2 == "show":
        for i in range(len(R)):
            for j in range(len(R)):
                print(str(R[i][j])+"\t", end='')
                if j == len(R) - 1: print("\n")
    
    if option1 == "time" or option2 == "time":
        print((end-start)*1000)
    


if __name__ == "__main__":
    main()