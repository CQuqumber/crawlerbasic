def check_diagonal(matr):
    k = 1
    L = len(matr)
    l = L -1
    while(k<L):
        if matr[0][0] == matr[k][k]:
            return False
        k = k + 1
    k = 1
    L = len(matr)
    l = L - 1
    while(k<L):
        if matr[0][L-1] == matr[k][L-1-k]:
            return False
        k = k + 1
    return True