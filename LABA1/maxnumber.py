def maxNumber(L):
    maxLength = len(str(max(L)))
    L = map(str, L)

    def sortKey(s):
        return s + s[-1] * (maxLength - len(s))

    sortedList = sorted(L, key=sortKey, reverse=True)
    return ''.join(sortedList)

print(maxNumber([10,2]))
print(maxNumber([3,30,34,5,9]))
print(maxNumber([10]))
print(maxNumber([1]))
print(maxNumber([99, 909, 59, 95, 910, 190]))