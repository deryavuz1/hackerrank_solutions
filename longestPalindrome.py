    def longestPalindrome(self, s: str) -> str:
        # if string is small, return itself
        if len(s) < 2:
            return s
        
        # helper function to perform the expansion from center
        def expand_from_center(left: int, right: int) -> str:
            # find palindrome, expand left and right from center until no longer
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # adjust the left index from being out of bounds
            # right is excluded - slicing is exclusive in python
            return s[left+1:right]

        longest = ""

        # palindrome's even or odd matters
        for i in range(0, len(s)):
            # even palindrome centers around 2 characters
            even = expand_from_center(i,i+1)
            # odd palindrome centers around 1 character
            odd = expand_from_center(i,i)

            # change the longest found 
            if len(even) > len(longest):
                longest = even
            if len(odd) > len(longest):
                longest = odd
        
        return longest
