# encode = utf8
import time
start = time.time()

# main
fi = open('input.txt', 'r')
fo = open('output.txt', 'w+')
n = int(fi.readline().replace('\n', ''))

def gcd(x, y):
    if (y == 0):
        return x
    elif (x % y == 0): 
        return y
    return gcd(y, x % y)
def verify(x, y):
    return x > 0 and gcd(x, abs(y)) == 1
def relation_number(x, y, n):
    if (verify(x, y) == 1):
        m = 0
        print('t')
        dn = 0
        while(m <= max(abs(y), x)):
            m += 1
            dy = -m
            while (dy <= m):
                if (abs(dy) == m):
                    for i in range(abs(dy), 0, -1):
                        dx = i
                        if (verify(dx, dy)): 
                            dn += 1
                            print(dx, dy, dn, 'a', m, n,y,x)
                            if (dx == x and dy == y): 
                                return dn
                else:
                    dx = abs(m)
                    if (verify(dx, dy)): 
                        dn += 1
                        print(dx, dy, dn, 'b',m,n,y,x)
                        if (dx == x and dy == y): 
                            return dn
                dy += 1
    return 0
for i in range(n):
    row = fi.readline().replace('\n', '').split(' ')
    dy = int(row[0])
    dx = int(row[1])
    n = 0    
    fo.write(str(relation_number(dx, dy, n)) + "\n")
fo.close()
fi.close()
    
#end

end = time.time()
print(end - start)
