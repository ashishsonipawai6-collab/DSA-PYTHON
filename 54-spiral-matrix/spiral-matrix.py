class Solution(object):
    def spiralOrder(self, matrix):

        m = len(matrix)
        n = len(matrix[0])
        srow = 0
        scol = 0
        erow = m-1
        ecol = n-1
        ans = []

        while srow <= erow and scol <= ecol:


        #top
            for j in range(scol, ecol+1):
                ans.append(matrix[srow][j])
            srow +=1
        #right
            for i in range(srow, erow+1):
                ans.append(matrix[i][ecol])
            ecol -=1
        #bottom
            if srow <= erow:
                for j in range(ecol, scol-1, -1):
                    ans.append(matrix[erow][j])
                erow -=1
        #left
            if scol <= ecol:
                for i in range(erow, srow-1, -1):
                    ans.append(matrix[i][scol]) 
                scol +=1

        return ans