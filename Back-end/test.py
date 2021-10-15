

def aaa(a):
    a[1] = a[1][0]
    return a

aa = [{1: {0: "ia"}}, {1: {0: "ia"}}]
a = list(map(aaa, aa))
print(a)
