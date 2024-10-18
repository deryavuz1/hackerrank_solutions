def alternatingCharacters(s):
    
    str1 = list(s)
    counter = 0
    
    for index in range(1, len(s)):
        if str1[index] == str1[index-1]:
            counter += 1
    return counter
