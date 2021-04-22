#MeMoization. The idea is to store the values, or better, to cache values
# in the base fibonacci the progtamm will slow down inreasing the sequence of terms

#in Memoization we cache the values for future clall

'''1: explicity Memoization'''

fibonacci_cache={} #will store recent fuction calls

def fibonacci(n):
    if type(n)!=int:
        raise TypeError('Input value of the Fibonacci series must be an integer')
    if n < 1:
        raise ValueError('Input value of the Fibonacci series must be positive')
    #if we have the cached values, then return it 
    if n in fibonacci_cache:
        return fibonacci_cache[n]
        #compute the n-th term
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)
    #cache the value and return it 
    fibonacci_cache[n] = value
    return value

def main():
    for n in range(1,101):
        print(f'{n}: {fibonacci(n)}')
if __name__=='__main__':
    main()
