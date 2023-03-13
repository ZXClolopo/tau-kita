#примо
n = 8
t = [[0, 2, 2, 0,  7, 0,  0,  0],
     [2, 0, 2, 9,  2, 0,  0,  0],
     [2, 2, 0, 0,  5, 0,  0,  0],
     [0, 9, 0, 0, 10, 5,  2,  16],
     [7, 2, 5, 10, 0, 0,  9,  0],
     [0, 0, 0, 5,  0, 0,  0,  17],
     [0, 0, 0, 2,  9, 0,  0,  17],
     [0, 0, 0, 16, 0, 17, 17, 0]]
g1 = ""
sum = 0
i = 0
while len(g1) < n:
     a = 100
     k = 0
     l = 0
     for j in range(n):
          if t[i][j] != 0 and t[i][j] < a and (g1.count(str(i)) == 0 or g1.count(str(j)) == 0):
               a = t[i][j]
               l = i
               k = j
               for s in range(n):
                    if t[s][k] != 0 and t[s][k] < a and g1.count(str(s)) > 0:
                         a = t[s][k]
                         l = s
     if l != i:
          i = l
     if g1.count(str(i)) == 0:
          g1 += str(i)
     if g1.count(str(k)) == 0:
          g1 += str(k)
     sum += a
     i = k
print(sum)
#Краскала
l = ['ab', 'ac', 'ae', 'ce', 'be', 'bd','eg', 'ed', 'gh', 'gd', 'dh', 'df', 'fh']
c = [2, 2, 7, 5, 2, 9, 9, 10, 17, 2, 16, 5, 17]
d = {}
for i in range(len(c)):
    d[l[i]] = c[i]
s = {}
sorted_keys = sorted(d, key=d.get)
for w in sorted_keys:
    s[w] = d[w]
sum = 0
h = ''
for i in s:
    if h.count(i[0]) < 1 and h.count(i[1]) < 1 and len(h) == 0:
        h += i
        sum += s[i]
    elif h.count(i[0]) < 1 and h.count(i[1]) < 1 and len(h) != 0:
        sum += s[i] + min(s[h[-1] + i[0]], s[h[-1] + i[1]])
        h += i
    elif h.count(i[0]) < 1:
        h += i[0]
        sum += s[i]
    elif h.count(i[1]) < 1:
        h += i[1]
        sum += s[i]
print(sum)