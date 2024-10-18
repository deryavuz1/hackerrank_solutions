def isValid(s):
    dict = {}
    arr = list(s)
    valid = False
    
    for i in arr:
        if i in dict.keys():
            dict[i] = 1 + dict[i]
        else:
            dict[i] = 1
    
    vals = set()
    
    for j in list(dict.values()):
        vals.add(j)
        
    # frequency counts
    # if set contains 1 value - they are all equal
    # if set contains 2 values - we remove one and should be good
    # if set contains 3 - no good
    if len(vals) == 1:
        return "YES"
    elif len(vals) == 2:
        return "YES"
    elif len(vals) > 2:
        return "NO"


def isValid(s):
    if len(s) == 1:
        return "YES"
    freq = dict()
    for c in s:
        if c not in freq.keys():
            freq[c] = 1
        else:
            freq[c] += 1
    values = sorted(freq.values())
    print(values)
    # the index that we will remove will be the singular character with a count of 1 and all other characters are identical in frequency
    if values[0] == 1 and values[1] == values[-1]:
        return "YES"
    return "YES" if (values[0] == values[-1]) or (values[-1] - values[0] == 1 and (values.count(values[0]) == (len(values) - 1) or (values.count(values[-1]) == (len(values) - 1)))) else "NO
