from .alphabet import alphabet

def transition_matrix(bigrams):
    n = len(alphabet)

    #Inicializace matice TM o rozměru n x n s jednotkovými hodnotami; řádky a sloupce pojmenujeme podle znaků v alphabet
    TM = create_matrix(n, n)
    for bigram in bigrams:
        c1 = bigram[0]
        c2 = bigram[1]
        i = alphabet.index(c1)
        j = alphabet.index(c2)
        TM[i][j] += 1

    #Abychom se vyhnuli log(0) v dalších výpočtech, nuly nahradíme hodnotou 1
    for i in range(n):
        for j in range(n):
            if TM[i][j] == 0:
                TM[i][j] = 1
        
    return TM

def create_matrix(n, m):
    matrix = []
    
    for i in range(n):
        col = []

        for j in range(m):
            col[j] = 0
        
        matrix[i] = col

    return matrix