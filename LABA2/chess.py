def findQueens(Queens=[0] * 8, i=0):

    if i == 8:
        arr = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                arr[i][Queens[i]] = 1
        print(Queens)
        return arr
    else:
        for j in range(8):

            if checkField(i, j, Queens):

                Queens[i] = j

                chessBoard = findQueens(Queens, i + 1)

                if chessBoard:
                    return chessBoard



def checkField(i, j, Queens):
    r = i
    c = j

    for k in range(i):
        if j == Queens[k]:
            return False

    while i >= 0 and j >= 0:
        if Queens[i] == j:
            return False
        i -= 1
        j -= 1

    while r >= 0 and c <= 7:
        if Queens[r] == c:
            return False
        r -= 1
        c += 1
    return True


findQueens()