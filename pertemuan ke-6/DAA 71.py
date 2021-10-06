def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms=30
if nterms <=0:
    print('Please enter a positive integer')
elif nterms==1:
    print('Fibonacci sequence upto',nterms,':')
    print(n1)
else:
    print('Fibonacci sequence:')
    for i in range(nterms):
        print(recur_fibo(i))
