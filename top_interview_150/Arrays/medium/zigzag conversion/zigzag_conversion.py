class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Initialize ans
        ans = ""

        if not numRows:
            return ans
        elif numRows == 1:
            return s

        for row in range(numRows):
            i = row
            start = True
            while i < len(s):
                ans += s[i]

                if start or row in [0, numRows-1]: 
                    len_side = numRows-row if numRows-row > 1 else numRows
                else:
                    len_side = row + 1

                i += (len_side)*2 - 2
                start = not start

        return ans