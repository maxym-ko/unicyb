# 14_2
s = [e for e in range(2, 20)]
print(s[3:9])

# 14_4
s = [e*e for e in range(1, 11)]
print(s)

# 14_6_7
s2 = s[:10]
print(s2)

# 14_6_8
s2 = s[9::-1]  # s2 = s[-1::-1]
print(s2)


# 14_8_a
def read_one():
    try:
        x = int(input())
        return 0, x
    except ValueError:
        return 1, None
    except KeyboardInterrupt:
        return 2, None


def input_list():
    list_1 = []
    res = read_one()
    while res[0] != 2:
        if res[0] == 0:
            list_1.append(res[1])
        res = read_one()
    return list_1


# 14_10_a
def read_one():
    try:
        x = int(input())
        return 0, x
    except ValueError:
        return 1, None
    except KeyboardInterrupt:
        return 2, None


def input_list(n):
    list_1 = []
    if n <= 0:
        return list_1
    res = read_one()
    while n != 0 and res[0] == 0:
        list_1.append(res[1])
        res = read_one()
        n -= 1
        if res[0] != 0:
            del s[:]
            raise RuntimeError
    return list_1


# 14_12
def add_element(list_1, element):
    if element in list_1:
        return list_1.index(element)
    else:
        list_1.append(element)
        return len(list_1) - 1


# 14_15
def count_positive(list_1):
    result = 0
    for element in list_1:
        if element > 0:
            result += 1
    return result


# 14_16
def return_index(list_1, element):
    list_2 = []
    for i, el in enumerate(list_1):
        if el == element:
            list_2.append(i)
    return list_2


#14_22
def min_positive(list_1):
    min = float('inf')
    for element in list_1:
        if min > element > 0:
            min = element
    return min if min != float('inf') else None
