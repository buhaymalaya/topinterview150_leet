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

def removeDuplicates(nums: list[int]) -> int:
    # Initialize the position pointer and count for occurrences
    k = 0  # points to the position where the next element should be placed
    count = 0  # counts occurrences of the current element

    for i in range(len(nums)):
        # If at the start or current element differs from the previous
        if i == 0 or nums[i] != nums[i - 1]:
            count = 1
        else:
            count += 1

    # Place the element if it appears at most twice
        if count <= 2:
            nums[k] = nums[i]
            k += 1

    return k

# Example usage
nums1 = [1, 1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]}{['_' for _ in range(k1, len(nums1))]}")

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]}{['_' for _ in range(k2, len(nums2))]}")


def removeDuplicates(nums: list[int]) -> int:
    # Initialize two pointers: one for the current position and one for result placement
    k = 0

    for num in nums:
        # Place the number if it's either one of the first two elements or not exceeding two occurrences
        if k < 2 or num != nums[k - 2]:
            nums[k] = num
            k += 1

    return k

# Example usage
nums1 = [1, 1, 1, 2, 2, 3]
k1 = removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]}{['_' for _ in range(k1, len(nums1))]}")

nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
k2 = removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]}{['_' for _ in range(k2, len(nums2))]}")
