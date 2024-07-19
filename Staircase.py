def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '#' * i)

if _name_ == "_main_":
    staircase(5)
