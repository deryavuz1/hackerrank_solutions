class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        answer = []

        if len(s) < len(p):
            return []

        counter1 = collections.Counter(p)
        counter2 = collections.Counter(s[0: len(p) - 1])

        for char in range(len(p)-1, len(s)):
            # include char in the current counter, do this by +1 
            counter2[s[char]] += 1
            # compare counters, if equal in frequency, anagram found
            if counter1 == counter2:
                #anagram found
                answer.append(char - len(p) + 1)
            # decrement count of the character at the start of the current window
            # length of current window: i -> len(p) - 1 => i - len(p) + 1
            counter2[s[char - len(p) + 1]] -= 1
            # remove the character if it ends up being 0 
            if counter2[s[char - len(p) + 1]] == 0:
                del counter2[s[char - len(p)+ 1]]

        return answer
