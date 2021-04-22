from functools import lru_cache

@Lru_cache(maxsize = 10000)
def fibonacci(n):
    if type(n)!=int:
        raise TypeError('Input value of the function must be an integer')
    if n < 1:
        raise ValueError('Input value of the fuction must be positive')
    if n==1:
        return 1
    elif n==2:
       return
    elif n>2:
       return fibonacci(n-1)+fibonacci(n-2)

def main():
    for n in range(1,101):
        print(f'{n}: {fibonacci(n)}')
if __name__=='__main__':
    main()
