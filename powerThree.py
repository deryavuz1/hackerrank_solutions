def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        #while divisible by 3:
        while n % 3 == 0:
            n //= 3 # divide by 3
        return n == 1
