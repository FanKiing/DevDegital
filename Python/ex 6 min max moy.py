from random import uniform
def minmaxmoy(a):
    maxi = max(a)
    mini = min(a)
    moy = (sum(li)) / 10

    return maxi, mini, moy

li = []
for i in range(10):
    num = (uniform(0,20))
    li.append(num)
print(li)
max, min, moy = minmaxmoy(li)

print(f"le nb maximal: {max}")
print(f"le nb minimal: {min}")
print(f"la moyenne est: {moy}")