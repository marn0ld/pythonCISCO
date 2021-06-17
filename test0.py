q = '13dsf6s21 34jljsfls adasdf 3421'
def n(s):
    sep = s.split()
    nums = []
    nonums = []
    for el in list(sep):
        if el.isdigit():
            nums.append(el)
        elif not el.isdigit():
            nonums.append(el)

    print("List with numbers:",nums)
    print("List without numbers:",nonums)

n(q)