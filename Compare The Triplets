def compare_triplets(a, b):
    a_score = 0
    b_score = 0
    for a_i, b_i in zip(a, b):
        if a_i > b_i:
            a_score += 1
        elif a_i < b_i:
            b_score += 1
    return [a_score, b_score]

if _name_ == "_main_":
    a = [5, 6, 7]
    b = [3, 6, 10]
    print(compare_triplets(a, b)
