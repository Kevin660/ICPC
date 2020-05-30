# encode = utf8
# 
import time
start = time.time()

# main
import math
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')

n = 0
num_list = []
for i in fi:
    s = i.replace("\n", "").split(" ") 
    n = int(s[0])
    if (len(s) == 2):
        if (num_list != []): fo.write(str(sum(num_list[::2])) + "\n")
        num_list = list(range(1, n + 1))
    else:
        if (n == 4):
            num_list.reverse()
        else:
            xi = num_list.index(int(s[1]))
            yi = num_list.index(int(s[2]))
            x = num_list[xi]
            y = num_list[yi]
            
            if (n == 1):
                del num_list[xi]
                num_list.insert(yi, x)
            elif (n == 2):
                del num_list[xi]
                num_list.insert(yi + 1, x)
            elif (n == 3):
                num_list[xi] = y
                num_list[yi] = x
fo.write(str(sum(num_list[::2])) + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
