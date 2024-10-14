def encryption(s):
    
    s = s.replace(" ", "")
    column = math.ceil(math.sqrt(len(s)))
    answer = []
    
    for i in range(column):
        print(s[i::column])
        answer.append(s[i::column])

    return " ".join(answer)
