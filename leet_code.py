"""
leet_code.py contains the leet code class.
"""
class LeetCode:
    def isPalindrome(self, x: int) -> bool:

        assert x >= -2**31 and x <= 2**31-1

        if x < 0:
            return False
        else:
            num_as_list = []
            while x >= 10:
                num_as_list = [x % 10] + num_as_list
                x //= 10
            num_as_list = [x % 10] + num_as_list
            lst = num_as_list[::-1]
            return num_as_list == lst

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        assert len(nums) >= 2 and len(nums) <= 1e+4

        assert -1e+9 <= target and target <= 1e+9 

        for i in range(len(nums)):
            assert nums[i] >= -1e+9 and nums[i] <= 1e+9
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
    def removeDuplicates(self, nums: list[int]) -> int:
        assert len(nums) >= 1 and len(nums)<= 3e+4
        for i in range(len(nums)):
            assert abs(nums[i]) <= 100
        i = 1;  k = 0; n = len(nums)
        while i < n:
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i] 
            i += 1
        k += 1
        return k

    
    def plusOne(self, digits: list[int]) -> list[int]:
        """Given a non-empty array of digits representing a non-negative integer, 
        this function increment one to the integer. 
        Args:
            digits (list[int]): A list of integers representing a non-negative integer.
        Returns:
            list[int]: A list of integers representing the incremented integer.
        Constraints:
            1 <= digits.length <= 100
            0 <= digits[i] <= 9        
            """
        n = len(digits); i = n - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                i -= 1
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits
        


        