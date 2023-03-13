k = float('Inf')
list = [[0, 7, 9, k, k, 14],
        [7, 0, 10, 15, k, k],
        [9, 10, 0, 11, k, 2],
        [k, 15, 11, k, 6, k],
        [k, k, k, 6, 0, 9],
        [14, k, 2, k, 9, 0]]
n = 0
count = 0
sum = 0
m = 4
flag = True
list_ver = list[n]
count_st = [n]
while count < len(list):
    i = n
    next = k
    for j in range(len(list)):
        if i == j or j in count_st:
            continue
        if list[i][j] + sum < list_ver[j]:
            list_ver[j] = list[i][j] + sum
            if next > list_ver[j]:
                next = list_ver[j]
                flag = True
        elif next > list_ver[j]:
            next = list_ver[j]
            flag = False
    for p in range(len(list_ver)):
        if p == i or p in count_st:
            continue
        elif list_ver[p] == next:
            n = p
    count_st.append(n)
    if not flag:
        sum = 0
    sum = next
    count += 1
print(list_ver[m])
