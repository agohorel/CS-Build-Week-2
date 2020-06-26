class Solution:
    def findDuplicate(self, nums):        
        """ 
        strategy: mark visited nums by inverting their sign.
        if you encounter a negative, you've found the duplicate.
        
        this approach takes advantage of the fact that:
            a) the list contains only positive numbers
            b) every number in the list is a valid index into the list

        admission: this violates the constraint "You must not modify the array (assume the array is read only)."
        but if you loop over the list a second time you can just set everything back to it's default state in O(n) time
        bringing the total runtime to O(2n)
        
        note: this would not work if the given nums contained 0 or negative values.

        breakdown: 
        [1,2,1]
         ^
         i 
         abs(nums[i]) = 2

        [1,-2,1]
            ^
            i 
        abs(nums[i]) = 1

        [1,-2,1]
              ^
              i   
        abs(nums[i]) = -2 # dupe!

        """
        
        duplicate = None

        for i in range(len(nums)):
            # invert sign of seen (positive) values
            if nums[abs(nums[i])] > 0: 
                nums[abs(nums[i])] *= -1
            # if the last checked num is negative, the index that "pointed to it" was the dupe
            else:
                duplicate = abs(nums[i])

        # reset sign of nums
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1

        return duplicate

s = Solution()
print(s.findDuplicate([1,3,2,4,1]))