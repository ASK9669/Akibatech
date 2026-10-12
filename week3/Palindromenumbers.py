class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = 0
        arr = list(str(x))
        y = len(arr) - 1

        while s < y:
            if arr[s] != arr[y]:
                return False
                break

            s += 1
            y -= 1

        return True