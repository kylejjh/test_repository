# 2.Display numbers at the odd indices of a list

def odd_indices(lst):
    result = []
    for i in range(1, len(lst), 2):
        result.append(lst[i])

    return result

def even_indices(lst):
    result = []
    for j in range(0, len(lst), 2):
        result.append(lst[j])

    return result

sample_list = [10, 20, 30, 40, 50, 60, 70, 80]
len_lst = len(sample_list)

print(len_lst)
print(sample_list[len(sample_list) - 1])
print("Numbers at odd indices:", odd_indices(sample_list))
print("Numbers at odd indices:", even_indices(sample_list))

