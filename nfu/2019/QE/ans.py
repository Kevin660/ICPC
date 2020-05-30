# encode = utf8
import time
start = time.time()

# main
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
for i in fi:
    n = int(i.replace('\n', ''))
    arr = [[1]] # n = 0
    for j in range(1, n + 1):
        temp = []
        for k in range(j + 1):
            temp.append([])
            for o in range(k + 1):
                ca = arr[k][o] if (len(arr) > k) else 0
                cb = arr[k - 1][o - 1] if (o > 0) and k > 0 else 0
                cc = arr[k - 1][o] if (len(arr[k-1]) > o) and k > 0 else 0
                temp[k].append(ca + cb + cc)
        arr = temp
    for j in arr:
        for k in range(len(j)):
            j[k] = str(j[k])
        fo.write(" ".join(j) + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
