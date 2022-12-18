'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    result = []
    if target in nums:
        if nums.count(target) < 2:
            return [nums.index(target), nums.index(target)]
        elif nums.count(target) > 2:
            first = nums.index(target)
            for num in range(len(nums) - 1, -1, -1):
                if nums[num] == target:
                    second = num
                    break
            return [first, second]
        result.append(nums.index(target))
        # noinspection PyTypeChecker
        nums[nums.index(target)] = None
        result.append(nums.index(target))
        return result
    else:
        return [-1, -1]


'''
5. Longest Palindromic Substring

Given a string s, return the longest 
palindromic substring in s.
'''

def longestPalindrome(s: str) -> str:
    palindrome = ''
    check = ''
    if s == s[::-1]:
        return s
    for i in range(len(s)):
        for j in range(len(s[i:]) - 1, -1, -1):
            if s[i:j + i + 1] == s[i:j + i + 1][::-1]:
                check = s[i:j + i + 1]
                if len(check) > len(palindrome):
                    palindrome = check
    return palindrome


'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
'''

def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height)-1
    result = []
    while i != j:
        if height[i] < height[j]:
            result.append(height[i]*(j-i))
            i+=1
        else:
            result.append(height[j]*(j-i))
            j-=1
    return max(result)


'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.
'''

def lengthOfLongestSubstring(s: str) -> int:
    result = ""
    pre_result = ""
    for letter in s:
        if letter in pre_result:
            if len(pre_result) > len(result):
                result = pre_result
            pre_result = pre_result[pre_result.index(letter) + 1:] + letter
        else:
            pre_result += letter
    return max(len(result), len(pre_result))


'''
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''

def searchInsert(nums: List[int], target: int) -> int:
    result = []
    if target in nums:
        return nums.index(target)
    else:
        for num in nums:
            if num > target:
                add = nums.index(num)
                [result.append(x) for x in nums[:add]]
                result.append(target)
                [result.append(x) for x in nums[add:]]
                return result.index(target)
    nums.append(target)
    return nums.index(target)


'''
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''

def majorityElement(nums: List[int]) -> int:
    set_list = set(nums)
    majority_element = 0
    majority_count = 0
    for element in set_list:
        if nums.count(element) > majority_count:
            majority_count = nums.count(element)
            majority_element = element
    return majority_element


'''
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''

def plusOne(digits: List[int]) -> List[int]:
    string_digit = ''
    for num in digits:
        string_digit += str(num)
    string_digit = int(string_digit)
    string_digit += 1
    string_digit = str(string_digit)
    result = [int(i) for i in string_digit]
    return result


'''
1337. The K Weakest Rows in a Matrix

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
'''

def kWeakestRows(mat: List[List[int]], l: int) -> List[int]:
    import operator
    result = {}
    count = 0
    answer = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                count += 1
        result[i] = count
        count = 0
    sorted_counts = sorted(result.items(), key=operator.itemgetter(1))
    sorted_result = {k:v for k, v in sorted_counts}

    for k,v in sorted_result.items():
        if v == sorted_result[k]:
            answer.append(k)

    return answer[:l]


'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(s: str) -> bool:
    openers = '([{'
    closers = ')]}'
    result = []
    if s[0] in closers or s[-1] in openers:
        return False
    for letter in s:
        if letter in openers:
            result.append(letter)
        else:
            if result == []:
                return False
            else:
                if closers.index(letter) == openers.index(result[-1]):
                    result.pop()
                else:
                    return False
    if result == []:
        return True
    else:
        return False


'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

def romanToInt(s: str) -> int:
        counts = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        result = 0
        check = 0
        for letter in s:
            if check >= counts[letter]:
                check = counts[letter]
                result += counts[letter]
            else:
                result += counts[letter] - check * 2
                check = counts[letter]
        return result


'''
Create a frame!

Given an array of strings and a character to be used as border, output the frame with the content inside.
Notes:
Always keep a space between the input string and the left and right borders.
The biggest string inside the array should always fit in the frame.
The input array is never empty.
'''

def frame(text, char):
    long = max(list(map(len, text))) + 4
    result = ''
    result += char * long + '\n'
    for string in text:
        if len(string) == long - 4:
            result += f'{char} {string} {char}\n'
        else:
            result += f'{char} {string}' + (' ' * (long - 4 - len(string))) + f' {char}\n'
    result += char * long
    return result


'''
Tribonacci Sequence

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, 
returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)    
'''

def tribonacci(signature, n):
    l = signature
    count = 0
    if n < 3:
        return signature[:n]
    else:
        for i in range(n - 3):
            signature = l[i:(i + 3)]
            count += sum(signature)
            l.append(count)
            count = 0
        return l

'''
Who likes it?

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' ' + 'likes this'
    elif len(names) > 1 and len(names) <= 3:
        return ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
    else:
        count = len(names) - 2
        return ', '.join(names[:2]) + ' and ' + str(count) + ' others like this'
