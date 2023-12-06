class Solution:
    def __init__(self):
        self.convert = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
    def intToRoman(self, num: int) -> str:
        ans = ""
    
        for n in sorted(list(self.convert.keys()), reverse=True):
            while num >= n:
                num -= n
                ans += self.convert[n]

        return ans