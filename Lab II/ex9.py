def spectatori_nu_vad(matrix):
    rezultat = []
    randuri = len(matrix)
    coloane = len(matrix[0])
    
    for i in range(1, randuri):
        for j in range(coloane):
            for k in range(i):
                if matrix[k][j] >= matrix[i][j]:
                    rezultat.append((i, j))
                    break
    
    return rezultat

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

rezultat = spectatori_nu_vad(matrix)
print(rezultat)
