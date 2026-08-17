#leetcode:1572
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n - 1 - i]
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]
        return total_sum
#leetcode: 498
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows=len(mat)
        col=len(mat[0])
        res=[]
        for d in range(rows+col-1):
            dia=[]
            r=0 if d<col else d-col+1
            c=d if d<col else col-1
            while r<rows and c>=0:
                dia.append(mat[r][c])
                r+=1
                c-=1
            if d%2==0:
                dia.reverse()
            res.extend(dia)
        return res  
#leetcode-1380
