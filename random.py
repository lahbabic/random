from threading import Thread
import time
res = 0

def pow2(x):
    global res
    res += pow(2, x)

def double(x):
    global res
    res += 2*x 

def rec(x):
    global res
    for i in range(0, x):
        t = Thread(target=pow2, args=(i,))
        t1 = Thread(target=double, args=(i,))
        t2 = Thread(target=rec, args=(x-1,))
        t3 = Thread(target=double, args=(res,))
        t.start()
        t1.start()
        t2.start()
        t3.start()
        res %= 10000

rec(5)
print(res)
