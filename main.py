class Solution:

    def __init__(self, x: int):
        self.x = x

    def reverse(self) -> int:

        if self.x < 0:
            x1 = self.x * (-1)
            x2 = str(x1)
            x3 = x2[::-1]
            x4 = int(x3) * (-1)

            if x4 in range(-2 ** 31, (2 ** 31) - 1):
                print(int(x4))
                return int(x4)

            else:
                return 0
        elif self.x > 0:
            x2 = str(self.x)
            x3 = x2[::-1]
            x4 = int(x3)

            if x4 in range(-2 ** 31, (2 ** 31) - 1):
                print(int(x4))
                return int(x4)

            else:
                return 0


obj = Solution(int(input("number:")))
# n = int(input("number:"))
obj.reverse()
