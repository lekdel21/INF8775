
import matrix
import time

with open('ex11_0', 'r') as f:
    m1 = [[int(num) for num in line.split(' ')] for line in f]
m1.pop(0)
with open('ex11_1', 'r') as f:
    m2 = [[int(num) for num in line.split(' ')] for line in f]
m2.pop(0)

start = time.time()

R = matrix.conv(m1, m2)

end = time.time()

print("CONVENTIONNEL:")
print(end - start)

print("\n")

start = time.time()

R = matrix.strassenSeuil(m1, m2, 10)

end = time.time()

print("STRASSEN:")
print(end - start)

