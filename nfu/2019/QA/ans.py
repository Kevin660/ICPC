# encode = utf8
# 0532
import time

start = time.time()

# main
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
m = int(fi.readline())
for i in range(m):
    n = int(fi.readline())
    ans = ''
    k = 1
    acu = 1
    while(True):
        if (acu % n == 0 or k > 12):
            break
        k += 1
        acu *= k
    if (k > 12):
        ans = 'no'
    else:
        ans = str(k) + '\n'
    fo.write(ans)
fo.close()
fi.close()
# end

end = time.time()
print(end - start)
