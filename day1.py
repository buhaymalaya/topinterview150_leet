# 88. Merge Sorted Array
# Easy


# You are given two integer arrays nums1 and nums2, 
# sorted in non-decreasing order, 
# and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

 

# Constraints:

#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109

 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# FROM MY UNDERSTANDING:

# THE PARAMETERS INCLUDE - 
# - TWO ARRAYS BOTH CONTAINING INTEGERS ONLY (CAN BE ASSORTED IN ANY WAY EXCEPT ASCENDING)
# - TWO INTEGERS (m, n) REPRESENTING AMOUNT OF ELEMENTS IN NUMS1, NUMS2
# OUTPUT SHOULD NOT BE RETURNED, INSTEAD NUMS1 THAT CONTAINS NUMS2, ASC
# DO NOT INCLUDE 0 IN THE MERGED OUTPUT

# create pointers 
# p1 for nums1, since indexes start at 0, pointer1 should be m-1
# same for nums2, pointer2 = n-1
# pointer for nums1 as merged arr should be (m+n)-1 because it has to be big enough to accommodate non 0 elements in both arr

# first define the pointers after function
# while loop to iterate through both arr as long as pointers are >= 0
# compare values of both pointers 
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        pointer_output = (m+n) - 1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]: # if the last value of nums1 is bigger than that of nums2
                nums1[pointer_output] = nums1[pointer1] # assign the last value for nums1 output with nums1[pointer1]
                pointer1 -= 1 # iterate down the arr since the loop is starting at the very end or last index until 0 is reached (see constraint of while loop)
            else:
                nums1[pointer_output] = nums2[pointer2] # unless the last value of nums2 is > than that of nums1
                pointer2 -= 1 # iterate down the array until 0 is reached
                
            pointer_output -=1



        