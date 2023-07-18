Problem :Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.


Solution : python3

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        seen = [0] * (N+1)
        for num in nums:
            if seen[num]:
                return num
            seen[num] = 1

# Time Complexity: O(n)
# Space Complexity: O(n)
