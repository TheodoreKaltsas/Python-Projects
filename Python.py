from pygame import *

name = "John"
age = 23

print("%s is %d years old." % (name, age))

#Simple fibonacci sequence in Python
class fib(object):
    def fib(self, n):
        a, b = 0, 1
        
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
            
        print()

fibo = fib()

fibo.fib(20000000)
