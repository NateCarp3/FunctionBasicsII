def countdown(n, l = []):
    if n==-1:

        return l
    else:
        l.append(n)
        return countdown(n-1, l)
        
print(countdown(5))
def printAndReturn(x):
    if x == []:
        return []
    else:
        print(x[0])
        return x[1]

print(printAndReturn(['x','y']))

def firstPlusLen(l):
    if l == []:
        return l
    else:
        return l[0] + len(l)

print(firstPlusLen([1,2,3,4]))

def ValGreater(l, z):
    x = l[1]
    def ValGreaterHelper(l, x, z):
        if len(l)<1:
            return z
        if l[0]>x :
            z.append(l[0])
            return ValGreaterHelper(l[1:], x, z)
        else:
            return ValGreaterHelper(l[1:], x, z)

    print(ValGreaterHelper(l, x, z))
print(ValGreater([5, 2, 3, 2, 1, 4], []))

def LenVal(x, y):
    if x == 0: 
        return []
    else:
        return [y] + LenVal(x-1, y)

print(LenVal(4, 7))


