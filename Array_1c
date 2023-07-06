Problem: A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

Solutin : Python3

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums.reverse()
            return
         

        i=len(nums)-1
        found = False
    
        while i>=1:
            if nums[i] > nums[i-1]:
                found = True
                break
            i-=1
        if not found:
            nums.reverse()
            return
        j=i
        i-=1

        min_greater_than_i=float('inf')
        min_index = -1
        while j <= len(nums)-1:
            if nums[j] > nums[i]:
                if nums[j] <= min_greater_than_i:
                    min_greater_than_i = nums[j]
                    min_index =j
            j+=1

            nums[i], nums[min_index] = nums[min_index], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
