# ---set--- #


# 18_1

a = {2, 7}

contains_five = 5 in a

b = set()
b.add(5)

size_a, size_b = len(a), len(b)

disjoint = a.isdisjoint(b)

is_subset = b <= a
union = a & b
intersection = a | b
difference = a - b
symmetric_difference = a ^ b

b |= a
size_b = len(b)

# 18_2

c = {x for x in range(2, 24)}  # or a = set(range(2, 24))
print(c)
c_square = {x * x for x in c}
print(c_square)


# 18_6

def f(a: set, b: set) -> set:
    res = set()
    for a_elem in a:
        if all((a_elem % b_elem for b_elem in b)):
            res.add(a_elem)
    # or res = {a_elem for a_elem in a if all((a_elem % b_elem for x in b))}
    return res


print(f({2, 4, 8}, {5, 6, 7}))

# 18_7

s = [1, 2, 2, 3, 3, 3]
different_values = len(set(s))

# ---dictionary--- #


# 18_10

a = {1: 2, 0: 3}

a[3] = 6

for el in a.keys(): print(el, end=" ")
print()
for el in a.values(): print(el, end=" ")
print()
for el in a.items(): print(el, end=" ")
print()

a[0] += 5

for el in sorted(a.keys()): print(el, a[el])
print()

contains_thirteen = 13 in a

a.pop(0)

a_size = len(a)


# 18_17

def f(s: list) -> dict:
    res = {}
    for el in s:
        if el in res:
            res[el] += 1
        else:
            res[el] = 1
    return res


print(f([1, 2, 2, 3, 3, 3]))


# 18_20

def reverse_f(f, y):
    res = []
    for k, v in f.items():
        if v == y:
            res.append(k)
    return res


s = [1, 2, 2, 3, 3, 3]
print(reverse_f(f(s), 1))
