class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        
        left = 0
        right = 0
        maxFruitLen = 0
        basket = {}

        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1
            

            while len(basket) > 2:
                basket[fruits[left]] -= 1

                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                
                left += 1

            maxFruitLen = max((right-left) + 1, maxFruitLen)

        
        return maxFruitLen