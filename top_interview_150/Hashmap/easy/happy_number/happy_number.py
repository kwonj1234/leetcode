class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {n : True}
        new_num = n

        while True:
            temp_n = new_num
            new_num = 0
            while temp_n > 0:
                i = temp_n % 10
                new_num += i * i
                temp_n = temp_n // 10

            if new_num == 1:
                return True
            elif new_num in memo:
                return False
            else:
                memo[new_num] = True
