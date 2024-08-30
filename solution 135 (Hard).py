class Solution135:
    def candy(self, ratings: list[int]) -> int:
        '''
        Повертає мінімальну кількість цукерок, яку можна роздати дітям за такими правилами:
        - Кожна дитина отримає хоча б одну цукерку;
        - Дитина отримує більше цукерок за сусіда з меншим рейтингом.

        ```
        candies: 2 1 4 3 2 1 2 3 1 2
          candy([6,5,8,6,3,1,6,8,0,5]) -> 21
        ```
        '''

        if len(ratings) < 2: return len(ratings)

        candies = curr_candy = 1
        high_rating, high_rating_pos = ratings[0], 0
        last_pos = len(ratings) - 1
        is_high = True

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                is_high = True
                curr_candy += 1
                high_rating, high_rating_pos = ratings[i], i
            
            elif ratings[i - 1] == ratings[i]:
                is_high = False

                if ratings[i] == high_rating:
                    high_rating_pos = i
                
                if i == last_pos or ratings[i] <= ratings[i + 1]:
                    curr_candy = 1

            elif ratings[i - 1] > ratings[i]:
                if curr_candy > 1:
                    curr_candy -= 1
                else:
                    candies += i - high_rating_pos

                if i == last_pos or ratings[i] <= ratings[i + 1]:
                    if curr_candy > 1:
                        candies -= (i - high_rating_pos - int(is_high)) * (curr_candy - 1)
                        curr_candy = 1
                    
                    high_rating, high_rating_pos = ratings[i], i
            
            candies += curr_candy

        return candies
            
s = Solution135()
print(s.candy([1,2,4,4,3]))