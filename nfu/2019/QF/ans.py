# encode = utf8
import time
start = time.time()

# main
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
n = int(fi.readline().replace('\n', ''))
for i in range(n):
    s = fi.readline().replace('\n', '')
    index = 0
    rc = -1
    lc = -1
    while (True):
        rc = s.find(']')
        lc = (s[rc - 1:0:-1].find('[') - rc + 1) * -1
        if (rc == -1): break
        t = int(s[lc - 1])
        inner_str = s[lc + 1:rc]
        s = s.replace(str(t) + '[' + inner_str + ']', inner_str * t)
    fo.write(s + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
