# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }

# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:

# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:

#     1 <= nums.length <= 3 * 104
#     -104 <= nums[i] <= 104
#     nums is sorted in non-decreasing order.

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
        
# modify the array in-place and ensure that each unique element appears at most twice. use a two-pointer technique to achieve this with O(1) extra space:

# Plan:
# Use a slow pointer to track the index where the next valid element should be placed.
# Use a fast pointer to iterate through the array.
# For each element, if it is the first or second occurrence, copy it to the position indicated by slow and increment slow.
# Skip over additional duplicates beyond the second occurrence.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        # start with the first two elements (since we are allowed two occurrences).
        slow = 2
        
        for fast in range(2, len(nums)):
            # compare current element with the element two positions back.
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
                
        return slow

if __name__ == "__main__":
    # create an instance of the Solution class
    solution = Solution()

    # test case 1
    nums1 = [1,1,1,2,2,3]
    k1 = solution.removeDuplicates(nums1)
    print(f"Output for nums1: {nums1[:k1]}, k = {k1}")

    # test case 2
    nums2 = [0,0,1,1,1,1,2,3,3]
    k2 = solution.removeDuplicates(nums2)
    print(f"Output for nums2: {nums2[:k2]}, k = {k2}")

# Time Complexity:
# O(n) since we're iterating through the array once, where n is the length of nums.
# Space Complexity:
# O(1) since we are modifying the array in place without using any additional data structures.

# alternate solution

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        # initialize a pointer to store the position of the next unique element
        j = 1
        
        # iterate through the list starting from the second element
        for i in range(2, len(nums)):
            # if the current element is different from the element two places back
            if nums[i] != nums[j - 1]:
                j += 1  # move the pointer forward
                nums[j] = nums[i]  # place the current element in the next valid position

        return j + 1


