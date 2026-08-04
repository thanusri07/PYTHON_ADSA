  #Leetcode:1248
lass Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def most(k):  #most(3) & most(3-1=2)
            if k<0:
                return 0
            left,right=0,0
            odd=0
            count=0
            for right in range(len(nums)):
                if nums[right]%2==1:
                    odd+=1
                while odd>k:
                    if nums[left]%2==1:
                        odd-=1
                    left+=1
                count+=right-left+1
            return count
        return most(k)-most(k-1)
                