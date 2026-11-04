class Solution:
    def primePalindrome(self, n: int) -> int:

        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2

            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2

            return True

        if 8 <= n <= 11:
            return 11

        # Generate odd-length palindromes
        for length in range(1, 10, 2):

            start = 10 ** ((length - 1) // 2)
            end = 10 ** ((length + 1) // 2)

            for x in range(start, end):
                s = str(x)
                palindrome = int(s + s[-2::-1])

                if palindrome >= n and isPrime(palindrome):
                    return palindrome