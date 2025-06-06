# Leet Code problems

This repository contains Python solutions to various LeetCode problems, implemented in the [`LeetCode`](leet_code.py) class in [leet_code.py](leet_code.py).

## Features

- Palindrome check for integers
This function takes an integer and check wether or not it is a palindrome. 
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.isPalindrome(121))
```
Output: True

- Two sum problem solver
Given an integer array nums and an integer target, this function returns indices of the two numbers such that they add up to target.
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.twoSum([2,7,6,1,4], 6))
```
Output: [0, 4]

- Remove duplicates from sorted array
This function removes all duplicates in a list and returns the number of unique elements 
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.removeDuplicates([1,1,1,1,2,2,3,3,4,4,5,6,7,7,8,8,9]))

# The array will become: [1,2,3,4,5,6,7,8,9]
```
Output: 9
- Increment integer represented as a list of digits
This function take a list of digits of a number and increment it. The result is still a list.
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.plusOne([9]))
```
Output: [1,0]
- Integer square root calculation
This compute the squared root of a number and returns its integer part. The algorithm implements the sequence
$$u_{n+1} = \frac{1}{2}\left(u_n + \frac{x}{u_n}\right)$$ which we know converges to $\sqrt{x}$
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.mySqrt(20))

# The squared root of 20 is 4.47213595  
```
Output: 4
- Find median of two sorted arrays
This function takes two sorted arrays and find the median of the two.
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.findMedianSortedArrays([1,2],[3,4]))
```
Output: 2.5

- Integer to Roman numeral conversion  
This function converts an integer to its Roman numeral representation.  
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.intToRoman(1994))
```
Output: "MCMXCIV"

- Roman numeral to integer conversion  
This function converts a Roman numeral string to its integer value.  
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.romanToInt("MCMXCIV"))
```
Output: 1994

- Reverse integer  
This function reverses the digits of an integer. If reversing the integer causes it to go outside the signed 32-bit integer range, it returns 0.  
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.reverse(123))
print(new_obj.reverse(-456))
print(new_obj.reverse(1534236469))  # Example of overflow
```
Output:  
123 → 321  
-456 → -654  
1534236469 → 0 

- Integer division without using multiplication, division, or mod operator  
This function divides two integers and returns the quotient after dividing dividend by divisor. If the result overflows, it returns the maximum 32-bit signed integer value.
### Example
```python
from leet_code import LeetCode as lc

new_obj = lc()
print(new_obj.divide(10, 3))
print(new_obj.divide(7, -3))
print(new_obj.divide(-2147483648, -1))  # Example of overflow
```
Output:  
10 ÷ 3 → 3  
7 ÷ -3 → -2  
-2147483648 ÷ -1 → 2147483647

## Usage

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```
    python main.py
    ```

## File Structure

- [`leet_code.py`](leet_code.py): Contains the `LeetCode` class with problem solutions.
- [`main.py`](main.py): Example usage of the `LeetCode` class.
- [`requirements.txt`](requirements.txt): List of required Python packages.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.