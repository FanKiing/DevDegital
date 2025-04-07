from random import randint

"""myList=list()#[]
for i in range(10):
    myList.append(randint(1,20))"""
myList=[randint(1,20) for i in range(20)]

print(myList)
"""hexL=[]
for x in myList:
    hexL.append(hex(x))
print(hexL)"""
hexL=[hex(x) for x in myList]
print(hexL)
myDict=zip(myList,hexL)
print(dict(list(myDict)))


