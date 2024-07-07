# Question: You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0 
        r = k 
        final = sum(nums[l:r])
        current_val = final 
        while r < len(nums):
            current_val = current_val - nums[l] + nums[r]
            if current_val > final: 
                final = current_val 
            l += 1
            r += 1
        return final/k 

