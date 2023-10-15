def game(terra, power):
    result = power
    for i in terra :
        for j in i :
            if j <= power :
                result += j
    return result
print(game([[1,2,3,4],[2,3,4,1],[1,1,1,1]],2))                   