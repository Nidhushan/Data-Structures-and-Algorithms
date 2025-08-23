class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_len = 0
        left = 0
        basket = {}

        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left+=1
            max_len = max(max_len, (right-left+1))


        return max_len


        # nof = 0
        # max_nof = 0
        # left, right = 0, 0
        # N = len(fruits)
        # di = {}
        # while right<N:
        #     di[fruits[right]] = di.get(fruits[right], 0) + 1
        #     nof +=1
        #     while len(di)>2:
        #         nof -= 1 
        #         di[fruits[left]] -= 1
        #         if di[fruits[left]] == 0:
        #             del di[fruits[left]]
        #         left+=1

        #     max_nof = max(max_nof, nof)
        #     right+=1
        
        # return max_nof
            

        """
        Question:
        fruits --> arr

        You have 2 baskets, they can hold only one type of fruit.
        return max number of fruits that can be held.

        Solution:
            loop through fruits
            window - increment right - if same type (upto 2 types of fruits)
                - increment left - if more than 2 types of fruits
            return max number of fruits
        """