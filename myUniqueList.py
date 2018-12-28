myUniqueList = []
myLeftovers=[]
def Addtolist(number):
    if number not in myUniqueList:
        myUniqueList.append(number)
        return True
    else:
        myLeftovers.append(number)
        return False

Addtolist(5)
Addtolist(6)
Addtolist(7)
Addtolist(5)
Addtolist(4)
Addtolist(7)
print(myLeftovers)
print(myUniqueList)


