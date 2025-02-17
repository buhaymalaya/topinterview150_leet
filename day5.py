# # # Best Time to buy and sell stock

# # You are given an array prices where prices[i] is the price of a given stock on the ith day.

# # You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# # Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update min_price to the lowest price seen so far
            min_price = min(min_price, price)
             # Calculate profit if sold at current price
            profit = price - min_price
            # Update max_profit if this profit is higher than current max_profit
            max_profit = max(max_profit, profit)

        return max_profit
    
    # Create an instance of the Solution class
solution = Solution()

# Test cases
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print("Maximum profit for prices1:", solution.maxProfit(prices1))  # Expected output: 5
print("Maximum profit for prices2:", solution.maxProfit(prices2))  # Expected output: 0


# two pointer

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0  # Buy pointer
        max_profit = 0
        
        # Iterate with the right pointer starting from the second day
        for right in range(1, len(prices)):
            # If current price is less than the price at the buy pointer, move left to right
            if prices[right] < prices[left]:
                left = right
            else:
                # Calculate profit and update max_profit if it's higher
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit