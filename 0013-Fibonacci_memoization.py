import time

def fibonacci_simple(n):
    if n in [0,1]:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


def fibo(n, fib=[]):
    if len(fib) <=n : 
        fib=['' for x in range(n+1)] 
    if n in [0,1]:
        fib[n]=n
    else:
        if fib[n]:
            return fib[n]
        else:
            fib[n]= fibo(n-1, fib) + fibo(n-2, fib)
    print(f' len {len(fib)} - {fib}')
    return fib[n]

def fibodict(n, fib={}):
    #if len(fib) <=n : 
    #    fib=['' for x in range(n+1)] 
    if n in [0,1]:
        fib[n]=n
    else:
        if n in fib:
            return fib[n]
        else:
            fib[n]= fibo(n-1, fib) + fibo(n-2, fib)
    print(f' len {len(fib)} - {fib}')
    return fib[n]

class cal_fibo(object):
    def __init__(self):
        self.value={}

    def calculate(self, n):
        if n in [0,1]:
            return n
        if n in self.value:
            return self.value[n]

        self.value[n]=self.calculate(n-1)+self.calculate(n-2)
        #print(self.value)

        return self.value[n]

def fibocall(n):
    return cal_fibo().calculate(n)


## FASTEST, take the values to global

class cal_fibonacci(object):
    def __init__(self, value={}):
        self.value=value

    def __repr__(self):
        return f'call calculate(n) to generate a fibonacci sequence of n '

    def calculate(self, n):
        if n in [0,1]:
            return n
        if n in self.value:
            return self.value[n]
        else:
            self.value[n]=self.calculate(n-1)+self.calculate(n-2)

        return self.value[n]

my_value={}
def fibonacci(n):
    #print(f'n : {n}')
    return cal_fibonacci(my_value).calculate(n)


start = time.time()
#print(fibo(70))
print(fibodict(10))

interval = time.time()
#print(fibo(60))
#print(fibonacci(100))
print(f'fibonacci: {interval-start}')
oh = cal_fibonacci()
print(oh)
#print(cal_fibo().calculate(10))
for x in range(1,50):
    #print(f'for n={x} : {fibocall(x)}')
    print(f'for n={x} : {fibonacci(x)}')

end = time.time()
#print(fib)
print(f'fibonacci : {end-interval}')

#test.assert_equals(fibonacci(70), 190392490709135)
#test.assert_equals(fibonacci(60), 1548008755920)
#test.assert_equals(fibonacci(50), 12586269025)
