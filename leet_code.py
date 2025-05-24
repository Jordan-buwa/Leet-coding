"""
leet_code.py contains the leet code class. 
This class contains methods to solve various leet code problems.
The methods include:
1. isPalindrome: This method checks if a given integer is a palindrome.
2. twoSum: This method finds two numbers in a list that add up to a given target.
3. removeDuplicates: This method removes duplicates from a sorted list in-place.
4. plusOne: This method increments a non-negative integer represented as a list of digits by one.
5. mySqrt: This method computes the integer square root of a non-negative integer. Returns the integer part of the square root.

"""
class LeetCode:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, this function returns true if x is a palindrome,
        and false otherwise.
        Args:
            x (int): An integer.
        Returns:
            bool: True if x is a palindrome, False otherwise.
        Constraints:
            -2^31 <= x <= 2^31 - 1
        """

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
        """Given an integer array nums and an integer target, this function
           returns indices of the two numbers such that they add up to target.
        Args:
            nums (list[int]): A list of integers.
            target (int): An integer target.
        Returns:
            list[int]: A list of two integers representing the indices of the two numbers.
        Constraints:
            2 <= nums.length <= 10^4
            -10^9 <= nums[i] <= 10^9
            -10^9 <= target <= 10^9
        """
        assert len(nums) >= 2 and len(nums) <= 1e+4

        assert -1e+9 <= target and target <= 1e+9 

        for i in range(len(nums)):
            assert nums[i] >= -1e+9 and nums[i] <= 1e+9
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i,j]
        return None
    def removeDuplicates(self, nums: list[int]) -> int:
        """Given a sorted array nums, this function removes the duplicates in-place such that each element
        appears only once and returns the new length.
        Args:
            nums (list[int]): A sorted list of integers.
        Returns:
            int: The new length of the array after removing duplicates.
        Constraints:
            0 <= nums.length <= 3 * 10^4
            -100 <= nums[i] <= 100
            nums is sorted in ascending order.
        """
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
    
    def mySqrt(self, x: int) -> int:
        tol = 1e-9
        """
        We are going to iteratively determine the squared root of x
        The sequence will be u(t+1) = 0.5*(u(t)+x/u(t))
        Args:
            x (int): A non-negative integer.
        Returns:
            int: The integer part of the square root of x.
        Constraints:
            0 <= x <= 2^31 - 1
        """
        assert x >= 0 and x <= 2**31 - 1
        ut = x/2
        tem = 0; err = 1
        while err > tol:
            tem, ut = ut, ut
            ut = 0.5 * (ut + x/ut)
            err = abs(tem - ut) 
        return int(ut//1)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """Given two sorted arrays nums1 and nums2 of size m and n respectively,
        this function returns the median of the two sorted arrays.
        Args:
            nums1 (list[int]): A sorted list of integers.
            nums2 (list[int]): A sorted list of integers.
        Returns:
            float: The median of the two sorted arrays.
        """
        nums1 = list(nums1)
        nums2 = list(nums2)
        new_array = nums1 + nums2
        new_array.sort()
        n = len(new_array)
        if n % 2 == 0:
            return (new_array[n//2] + new_array[n//2 - 1])/2
        else:
            return new_array[n//2]
                
        