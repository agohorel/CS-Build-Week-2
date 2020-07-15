from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pointers to start/stop of each sorted sub-list
        low_1 = 0
        high_1 = self.find_range(nums)
        low_2 = high_1
        high_2 = len(nums)

        # attempt to find value in the larger of the two sub-lists
        if len(nums[low_1:high_1]) > len(nums[low_2:high_2]):
            result = self.binary_search(nums[low_1:high_1], target)
        else:
            result = self.binary_search(nums[low_2:high_2], target)
            # add the length of the first sub-list to the found index from the second sub-list
            result += len(nums[low_1:high_1])
        
        # if not already found, search the remaining sub-list 
        if result == -1:
            if len(nums[low_1:high_1]) > len(nums[low_2:high_2]): 
                result = self.binary_search(nums[low_2:high_2], target) 
                result += len(nums[low_1:high_1])
            else:
                result = self.binary_search(nums[low_1:high_1], target) 

            return result

        return result

    def binary_search(self, nums, target):
        low = 0
        mid = len(nums)//2
        high = len(nums)-1

        while low <= high:
            mid = (low + high)//2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                low = mid + 1
            elif guess > target:
                high = mid - 1
        return -1

    def find_range(self, nums):
        for idx, num in enumerate(nums):
            if num > nums[idx+1]:
                return idx+1
            

# nums = [4, 5, 6, 7, 0, 1, 2]
nums = [4, 5, 6, 0, 1, 2, 3]

s = Solution()
print(s.search(nums, 6))
print(s.search(nums, 1))
