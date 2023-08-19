class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [amount+1]*(amount+1)
        num_coins[0] = 0
        coins.sort()
        
        for amt in range(1, len(num_coins)):
            i = 0
            for i in range(len(coins)):
                if amt-coins[i] >= 0:
                    num_coins[amt] = min(num_coins[amt], (1+num_coins[amt-coins[i]]))
                
        print(num_coins)
        if num_coins[amount] < amount+1:
            return num_coins[amount]
        else:
            return -1
