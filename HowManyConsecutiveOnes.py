'''

Given a binary array nums, return the maximum number of consecutive 1's in the array.

'''

class Solution:
    def findMaxConsecutiveOnes(self,nums) -> int:
        txt = ''
        for i in range(len(nums)):
            txt += str(nums[i])
        
        return max(list(map(len,txt.split('0'))))

s = Solution()
print(s.findMaxConsecutiveOnes([0,1,1,0,0,1,1,1,0,0,1]))


