def plus_minus(arr):
    n = len(arr)
    positive = sum(x > 0 for x in arr) / n
    negative = sum(x < 0 for x in arr) / n
    zero = sum(x == 0 for x in arr) / n
    return f"{positive:.6f}\n{negative:.6f}\n{zero:.6f}"

if _name_ == "_main_":
    arr = [-4, 3, -9, 0, 4, 1]
    print(plus_minus(arr))
