def transposematrix(matrix):
# transpose an n column by n row matrix
# ie: transposematrix([[a,b],[c,d]]) -> [[a,c],[b,d]]

    #layer by layer approach
    for j in range(len(matrix)):
        for i in range(j+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

test1 = [[1,2,3],[4,5,6]]
print(transposematrix(test1))
            
        
