#Leet code:1351
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]<0:
                    count+=1
        return count

#Leet code: 832
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        '''
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[0])):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image
        '''
        for row in image:
            left=0
            right=len(row)-1
            while left<=right:
                row[left],row[right]=1-row[right],1-row[left]
                left+=1
                right-=1
        return image

    