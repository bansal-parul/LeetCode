class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = sum(cost)
        total_gas = sum(gas)
        if total_cost> total_gas:
            return -1
        tank = 0
        index = 0
        for i in range(len(gas)):
            tank = tank+gas[i] - cost[i]
            if tank <0:
                tank = 0
                index = i+1
        return index
            
        
