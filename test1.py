#на вхід приймає рядок
q = 'arno31 muke231 mogas'


def stringcheck(s):
    sep = s.split()
    sep2 = " ".join(sep)
    print("-" * 45)
    print("String:", sep2)

    nums = []
    letters = []

    for el in list(q):
        if el.isdigit(): #виділяє з нього всі числа в окремий масив
            nums.append(el)
            nums2 = "".join(nums)
        else:
            letters.append(el)
            letters2 = "".join(letters)
    print("-"*45)
    #після чого програма друкує рядок без чисел і масив чисел
    print("List with numbers:", int(nums2))
    print("List without numbers:", letters2)

    print("-" * 60)
    #Змінити цей рядок таким чином, щоб кожне слово в ньому, починалось і закінчувалось великою літерою
    letterers = []
    letters2, letters3 = letters2.title(), ""
    for i in letters2.split():
        letters3 += i[:-1] + i[-1].upper() + " "
        letterers.append(letters3[:-1])
    print("First and last letters capitalized:", letterers[-1])

    print("-" * 60)
    #Знайти максимальне значення в масиві чисел
    print("Max number in a number array:", int(max(nums2)))
    #всі інші числа піднести до степеню по їх індексу, та записати в інший масив
    res = []
    for el2 in list(nums2):
        if int(el2) != int(max(nums2)):
            power = int(el2) ** int(el2)
            res.append(power)

    print("Self-powered numbers:", res)

    print("-" * 60)


stringcheck(q)
