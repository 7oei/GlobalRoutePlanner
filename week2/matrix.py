import numpy, sys, time
import matplotlib.pyplot as plt 

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

cnt = int(sys.argv[1])
ans = []
t = 5
for n in range(1,cnt):
    sum = 0
    for p in range(t):
        a = numpy.zeros((n, n)) # Matrix A
        b = numpy.zeros((n, n)) # Matrix B
        c = numpy.zeros((n, n)) # Matrix C

        for i in range(n):
            for j in range(n):
                a[i, j] = i * n + j
                b[i, j] = j * n + i
                c[i, j] = 0

        begin = time.time()

        for i in range(n):
            for j in range (n):
                for k in range(n):
                    c[i, j] += a[i, k] * b[k, j]

        end = time.time()
        print("time: %.6f sec" % (end - begin))
        sum += end - begin
    ans.append(sum/t)

        # # Print C for debugging. Comment out the print before measuring the execution time.
        # total = 0
        # for i in range(n):
        #     for j in range(n):
        #         # print c[i, j]
        #         total += c[i, j]
        # # Print out the sum of all values in C.
        # # This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
        # print("sum: %.6f" % total)
print(ans)
plt.plot(ans)
plt.savefig("matrixMulTimeAve3")