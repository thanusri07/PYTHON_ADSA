#leet code:54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        if not matrix:
            return res
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res

#leet code: 59
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[0]*n for i in range(n)]
        top=0
        bottom=n-1
        left=0
        right=n-1
        num=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res[top][i]=num
                num+=1
            top+=1
            for i in range(top,bottom+1):
                res[i][right]=num
                num+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res[bottom][i]=num
                    num+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res[i][left]=num
                    num+=1
                left+=1
        return res