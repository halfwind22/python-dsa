# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

from datetime import datetime
from typing import List


class Solution:

    def removeDuplicatesEfficient(self, nums: List[int]) -> int:

        global_counter = 1
        counter = 0
        ptr = 0
        for j in range(0,len(nums)):
            if nums[j]<=nums[ptr]:
                counter+=1
                if counter>2:
                    ptr=j
                    k = j+1
                
                    while k<len(nums):
                        if nums[k]>nums[ptr]:
                            stop = k
                            break
                        k+=1
    
                    for m in range(ptr,stop):
                        if nums[ptr]<nums[stop]:
                            nums[ptr] = nums[stop]
                    
                    counter = 1
                    global_counter+=2
            elif nums[j]>nums[ptr]:
                counter = 1
                global_counter+=2
                ptr = j
        return global_counter

nums = [0,0,0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,1,2,2,3]

soln = Solution()
print(datetime.now())
print(soln.removeDuplicatesEfficient(nums=nums))
print(datetime.now())

print(nums)


