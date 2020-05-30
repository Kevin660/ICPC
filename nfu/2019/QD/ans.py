# encode = utf8
# 0803
#
import time
start = time.time()

# main
import math
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
n = int(fi.readline().replace("\n", ""))
def f(e):
        return e[1] + e[0]
for i in range(n):
    m = int(fi.readline().replace("\n", ""))
    d = []
    for j in range(m):
        l = fi.readline().replace("\n", "").split(" ")
        if int(l[2]) <= 1000:
            d.append([l[0], l[1], l[2]])
    d = sorted(d, key=f)
    for j in d[:3]:
        fo.write(" ".join(j[:2]) + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
