import math

def get_total_x(a, b):
    lcm_a = a[0]
    for i in a[1:]:
        lcm_a = lcm_a * i
    gcd_b = b[0]
    for i in b[1:]:
        gcd_b = math.gcd(gcd_b, i)

    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    return count

if _name_ == "_main_":
    a = [2, 4]
    b = [16, 32, 96]
    print(get_total_x(a, b))
