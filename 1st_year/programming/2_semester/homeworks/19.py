from math import sqrt


# 19_5
def prime_less_n(n: int) -> set:
    res = {x for x in range(2, n)}
    for i in range(2, n):
        for j in range(2, int(sqrt(i) + 1)):
            if i % j == 0:
                res.remove(i)
                break
    return res
    # or return {num for num in range(2, n) if all(num % x for x in range(2, int(sqrt(num) + 1)))}


# 19_23b
def intersection(m: dict, n: dict) -> dict:
    res = {}
    for key in m.keys() & n.keys():
        res[key] = min(m[key], n[key])
    return res


print(prime_less_n(100))
print(intersection({5: 5, 6: 3, 8: 1}, {5: 2, 8: 3}))
