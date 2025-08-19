class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for row in accounts:
            max_wealth = max(sum(row), max_wealth)
        
        return max_wealth
        
        # for i in accounts:
        #     if sum(i)>max_wealth:
        #         max_wealth = sum(i)
        
        # return max_wealth

    """
    Question:
    You have an m x n list. 
    Each row is a customer
    each column is the amount that customer has in a bank.
    Return the richest customer(max wealth)

    have a max_wealth
    loop through each row:
        if sum(row)>max_wealth:
            max_wealth = sum(row)
        
    return max_wealth
    """