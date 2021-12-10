# 22_3 (22_2_b)
def f_22_3():
    import sys

    def read_to_list(filename):
        lst = []
        err_n = 0
        with open(filename) as f:
            for s in f:
                try:
                    s = s.strip()  # additional (to complete 22_3)
                    if s != '':  # additional (to complete 22_3)
                        lst.append(int(s))
                except ValueError as e:
                    err_n += 1
                    sys.stderr.write(repr(e) + '\n')
        return lst, err_n

    print(read_to_list("test.txt"))


# 22_6
def f_22_6():
    def write_lst(filename):
        lst = []
        with open(filename) as f:
            for s in f:
                if s.strip() != '':
                    try:
                        lst.append(int(s))
                    except ValueError:
                        lst.append(float(s))
        return lst

    print(write_lst("files/test.txt"))


# 22_7
def f_22_7():
    def analyze(filename):
        res = [0, 0, 0, 0]
        with open(filename) as f:
            for s in f:
                res[get_kind(s)] += 1
        return {'int_count': res[0], 'float_count': res[1], 'blank_count': res[2], 'err_count': res[3]}

    def get_kind(s):
        if s.isspace():
            return 2
        try:
            int(s)
            return 0
        except ValueError:
            try:
                float(s)
                return 1
            except ValueError:
                return 3

    print(analyze("files/test.txt"))


# 22_8
def f_22_8():
    def write_pairs_to_lst(filename):
        lst = []
        with open(filename) as f:
            for s in f:
                lst.append((float(s.split()[0]), float(s.split()[1])))
        return lst

    print(write_pairs_to_lst("files/test.txt"))


# 22_16(v)
def f_22_16():
    import sys
    sys.path.append('/home/maxym_ko/cyb/cyb_python/1_course/2_semester/lessons/files')
    from OutputStream import FloatInputStream

    def files_equals(filename1, filename2):
        flag = False
        with FloatInputStream(filename1) as r1, FloatInputStream(filename2) as r2:
            while flag:
                num1 = r1.read()
                num2 = r2.read()
                flag = num1 is not None and num2 is not None and num1 == num2
        return num1 == num2


# 22_18
def f_22_18():
    import sys
    sys.path.append('/home/maxym_ko/cyb/cyb_python/1_course/2_semester/lessons/geo/geo')
    from point import Point

    def str2Point(s):
        i = s.find('(')
        j = s.rfind(')')
        if i == -1 or j == -1:
            return None
        lst = s[i+1: j].split(',')
        if len(lst) != 2:
            return None
        try:
            first_number = float(lst[0])
            second_number = float(lst[1])
            return Point(first_number, second_number)
        except ValueError:
            return None

    point = str2Point('(1,2)')
    point2 = str2Point('(!1,2)')
    point3 = str2Point('(1!,2)')
    point4 = str2Point('(1,,2)')

    if point is not None: print(point.x, point.y)
    else:
        print("Error")
    if point2 is not None: print(point2.x, point2.y)
    else:
        print("Error")
    if point3 is not None: print(point3.x, point3.y)
    else:
        print("Error")
    if point4 is not None: print(point4.x, point4.y)
    else:
        print("Error")


# 22_19
def f_22_19():
    import sys
    sys.path.append('/home/maxym_ko/cyb/cyb_python/1_course/2_semester/lessons/geo/geo')
    from point import Point

    def read_point(point):
        return f'({point.x}, {point.y})'

    print(read_point(Point(1, 2)))


# 22_32 (v, g, e)
def f_22_32():
    # BAD (rewrite)
    def _split(s):
        lst = list(filter(len, s.replace(' ', '.')
                          .replace(',', '.')
                          .replace(';', '.')
                          .replace(':', '.')
                          .replace('?', '.')
                          .replace('!', '.')
                          .split('.')))
        return lst

    def len_gt_three(s):
        lst = _split(s)
        # return len(list(filter(lambda x: len(x) > 3, lst)))
        return len([el for el in lst if len(el) > 3])

    def len_eq_thirteen(s):
        lst = _split(s)
        # return len(list(filter(lambda x: len(x) == 13, lst)))
        return len([el for el in lst if len(el) == 13])

    def last_len_thirteen(s):
        lst = _split(s)
        # tmp = list(filter(lambda x: len(x) == 13, lst))
        tmp = [el for el in lst if len(el) == 13]
        return tmp[-1] if len(tmp) > 0 else None

    print(len_gt_three('     one, two ;; three; ;;four!!   five? six seven  eight: nine;'))
    print(len_eq_thirteen('     one, twofkfkfkfkfk ;; three; ;;four!!   five? six seveffffffffn  eight: nine;'))
    print(last_len_thirteen('     one, twofkfkfkfkfk ;; three; ;;four!!   five? six seveffffffffn  eight: nine;'))
    print(last_len_thirteen('     one, sad ;; three; ;;four!!   five? six asd  eight: nine;'))


def main():
    f_22_3()


if __name__ == '__main__':
    main()