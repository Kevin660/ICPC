# encode = utf8
import time
start = time.time()

# main
import math
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
m = int(fi.readline())
for i in range(m):
    s = fi.readline().split(" ")
    b = int(s[0])
    e = int(s[1])
    ans = ''
    count = 0
    for j in range(b, e + 1):
        for t in range(int(math.log(j, 2)) , -1, -1):
            if (j >= 2**t): 
                j -= 2 ** t
                count += 1
    ans = str(count) + '\n'
    fo.write(ans)
fo.close()
fi.close()
#end

end = time.time()
print(end - start)
