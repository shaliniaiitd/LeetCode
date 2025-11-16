def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(6
          ))

def fact(n):
    if n ==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))