class Solution:
    def update_max_profit(self, start: int, cost: int, profit: int):
        for i in range(start, len(self.project_ids)):
            pr_i = self.project_ids[i]
            new_cost = cost + self.costs[pr_i]

            if new_cost > self.budget:
                self.max_profit = max(self.max_profit, profit)
                return
            
            new_profit = profit + self.profits[pr_i]
            
            self.update_max_profit(i + 1, new_cost, new_profit)
    

    def maxProfit(self, budget: int, costs: list[int], profits: list[int]) -> int:
        '''
        Повертає максимальний прибуток, який можно отримати з `n` проектів
        не виходячи за межі бюджету `budget`.

        `n = len(costs) = len(profits)`

        Кожен `i` проект коштує `costs[i]` та приносить дохід `profits[i]`
        '''
        
        self.budget = budget
        self.costs = costs
        self.profits = profits
        self.project_ids = sorted(range(len(costs)), key=lambda i: costs[i])

        self.max_profit = 0
        self.update_max_profit(0, 0, 0)

        return self.max_profit


s = Solution()
print(s.maxProfit(600, [200,400,800,200,300], [300,800,2000,400,350])) # -> 1200