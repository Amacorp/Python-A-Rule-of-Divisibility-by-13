array = [1, 10, 9, 12, 3, 4]

def thirt(n):
    total = sum([int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)
    
    
Or

import itertools as it

def thirt(n):
    if n < 100: return n
    
    pattern = it.cycle([1, 10, 9, 12, 3, 4])
    
    return thirt(sum(d*n for d,n in zip(map(int, str(n)[::-1]), pattern)))
    
    
OR



def thirt(n):
    w = [1, 10, 9, 12, 3, 4]
    while True:
        r = n; q = -1; c = 0; j = 0
        while (q != 0):
            q = int(r / 10)
            c += (r % 10) * w[j % 6]
            r = q
            j += 1
        if (c == n): return c
        n = c
        
        
        
 OR
 
 
 
 def thirt(n):
    p = [1, 10, 9, 12, 3, 4]
    ns = sum(int(c) * p[i % len(p)] for i, c in enumerate(str(n)[::-1]))
    return ns if ns == n else thirt(ns)
