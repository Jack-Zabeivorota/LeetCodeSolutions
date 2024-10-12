class Solution1942:
    def smallestChair(self, friends: list[list[int]], target_friend: int) -> int:
        '''
        Повертає номер місця, на якому буде сидіти `target_friend` при умовах, що
        кожен друг буде сидіти на першому вільному місці від 0-го місця, враховуючи
        час прибуття друга (`friends[i][0]`) та час його відходу (`friends[i][1]`).

        ```
        smallestChair([[2,4],[1,3],[3,6]], 2) -> 0

        ```
        '''

        target_friend_arrival = friends[target_friend][0]

        friends.sort(key=lambda x: x[0])
        chairs: list[list[int]] = []

        for friend in friends:
            chair_idx = None

            for i in range(len(chairs)):
                if chairs[i][1] <= friend[0]:
                    chairs[i], chair_idx = friend, i
                    break
            
            if chair_idx is None:
                chairs.append(friend)
                chair_idx = len(chairs) - 1

            if friend[0] == target_friend_arrival:
                return chair_idx


s = Solution1942()
print(s.smallestChair([[3,10],[1,5],[2,6]], 0))