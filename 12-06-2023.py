class Solution:
    def cutRod(self, price, n):
        max_value = [0] * (n + 1)
        max_value[1] = price[0]
        
        for rod_length in range(2, n + 1):
            max_price = 0
            for cut in range(1, rod_length):
                max_price = max(max_price, max_value[cut] + max_value[rod_length - cut])
            max_price = max(max_price, price[rod_length - 1])
            max_value[rod_length] = max_price
        
        return max_value[-1]
