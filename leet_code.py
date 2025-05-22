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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        assert len(nums) >= 2 and len(nums) <= 1e+4

        assert -1e+9 <= target and target <= 1e+9 

        for i in range(len(nums)):
            assert nums[i] >= -1e+9 and nums[i] <= 1e+9
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
        