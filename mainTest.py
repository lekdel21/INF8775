import matrix
import time

def main():   

    # timeConv = 0
    # timeStrassen = 0

    # for i in range(2, 10):
    #     for j in range(0, 10, 2):
            
    #         with open("ex"+str(i)+"_"+str(j), 'r') as f:
    #             m1 = [[int(num) for num in line.split(' ')] for line in f]
    #         m1.pop(0)
    #         with open("ex"+str(i)+"_"+str(j+1), 'r') as f:
    #             m2 = [[int(num) for num in line.split(' ')] for line in f]
    #         m2.pop(0)
            
    #         start = time.time()
    #         R = matrix.conv(m1, m2)
    #         end = time.time()
    #         timeConv += end - start
    #         if j == 8:
    #             print("time Conv " + str(i) + ": " + str(timeConv/5))
    #             timeConv = 0
            
    #         start = time.time()
    #         R = matrix.strassen(m1, m2)
    #         end = time.time()
    #         timeStrassen += end - start
    #         if j == 8:
    #             print("time Strassen " + str(i) + ": " + str(timeStrassen/5))
    #             timeStrassen = 0

    for i in range(10, 11):
        
        with open("ex"+str(i)+"_0", 'r') as f:
            m1 = [[int(num) for num in line.split(' ')] for line in f]
            m1.pop(0)
        with open("ex"+str(i)+"_1", 'r') as f:
            m2 = [[int(num) for num in line.split(' ')] for line in f]
            m2.pop(0)
        
        # start = time.time()
        # R = matrix.conv(m1, m2)
        # end = time.time()
        # print("time Conv " + str(i) + ": " + str(end - start))

        start = time.time()
        R = matrix.strassenSeuil(m1, m2, 9)
        end = time.time()
        print("time Strassen " + str(i) + ": " + str(end - start))

if __name__ == "__main__":
    main()