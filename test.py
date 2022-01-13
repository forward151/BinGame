def count_sum(lst, syst):
    x = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            x += syst ** (len(lst) - i - 1)
    return x

print(count_sum([1, 1, 1, 1, 1, 1, 1, 1], 2))

def count_sum_2(lst):
    string = ''.join([str(i) for i in lst])
    x = int(string, 16)
    return x

print(count_sum_2(['A', 'F', 1, 9, 3, 'C', 'D', 1]))