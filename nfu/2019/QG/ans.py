# encode = utf8
import time
start = time.time()

# main
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
n = int(fi.readline().replace('\n', ''))

def cycle(current, arr, path, e):
    if (current in path):
        if(len(path) > 2 and current == path[0]):
            if (sorted(path) in e): 
                return []
            e += [sorted(path)]
            return 1
        else:
            return 0
    if (len(arr[current]) == 0): return 0
    p = []
    for i in range(len(arr[current])):
        if (arr[current][i] != current):
            cycle(arr[current][i], arr, path + [current], e)       
for i in range(n):
    kn = int(fi.readline().replace('\n', ''))
    km = int(fi.readline().replace('\n', ''))
    ci = []
    for i in range(kn):
        ci += [[]]
    for j in range(km):        
        d = fi.readline().replace('\n', '').split(" ")
        ci[int(d[0]) - 1].append(int(d[1]) - 1)
        ci[int(d[1]) - 1].append(int(d[0]) - 1)
    path = []
    for j in range(len(ci)):
        cycle(j, ci, [], path)
    s = "n"
    if (len(path) >= 3): s = "y: there are at least three cycles"
    if (len(path) == 2): s = "y"
    
    fo.write(s + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
