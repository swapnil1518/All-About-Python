def sqrt(n):
    for i in range(1,n+1):
        yield i*i
a = sqrt(3)
print(next(a))
print(next(a))
print(next(a))

# we want to get sqrt of 1 rto 3 nos