import matrix
import time

def main():   

    timeConv = 0
    timeStrassen = 0

    for i in range(10, 11):
        for j in range(0, 1, 2):
            
            with open("ex"+str(i)+"_"+str(j), 'r') as f:
                m1 = [[int(num) for num in line.split(' ')] for line in f]
            m1.pop(0)
            with open("ex"+str(i)+"_"+str(j+1), 'r') as f:
                m2 = [[int(num) for num in line.split(' ')] for line in f]
            m2.pop(0)
            
            start = time.time()
            R = matrix.strassenSeuil(m1, m2, 216)
            end = time.time()
            timeStrassen += end - start
            if j >= 0:
                print("time Strassen " + str(i) + ": " + str(timeStrassen/3))
                timeStrassen = 0
            
            start = time.time()
            R = matrix.conv(m1, m2)
            end = time.time()
            timeConv += end - start
            if j >= 0:
                print("time Conv " + str(i) + ": " + str(timeConv/3))
                timeConv = 0
            
            

    # for i in range(10, 11):
        
    #     with open("ex"+str(i)+"_0", 'r') as f:
    #         m1 = [[int(num) for num in line.split(' ')] for line in f]
    #         m1.pop(0)
    #     with open("ex"+str(i)+"_1", 'r') as f:
    #         m2 = [[int(num) for num in line.split(' ')] for line in f]
    #         m2.pop(0)
        
    #     # start = time.time()
    #     # R = matrix.conv(m1, m2)
    #     # end = time.time()
    #     # print("time Conv " + str(i) + ": " + str(end - start))

    #     start = time.time()
    #     R = matrix.strassenSeuil(m1, m2, 9)
    #     end = time.time()
    #     print("time Strassen " + str(i) + ": " + str(end - start))

if __name__ == "__main__":
    main()