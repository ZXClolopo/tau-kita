import pprint
inv = float('Inf')
list = [[0, 1, inv, inv, 6, 3],
        [1, 0, 6, inv, inv, 5],
        [inv, 6, 0, 1, 3, 3],
        [inv, inv, 1, 0, 2, inv],
        [6, inv, 3, 2, 0, 4],
        [3, 5, 3, inv, 4, 0]
        ]
for k in range(len(list)):
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                continue
            list[i][j] = min(list[i][k] + list[k][j], list[i][j])
pprint.pp(list)
