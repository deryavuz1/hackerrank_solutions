def freqQuery(queries):
    # 1 - insert
    # 2 - delete
    # 3 - contains
    freq_dict = {}
    return_list = []
    
    
    for query in queries:
        operation, value = query
        if operation == 1:
            # add AKA add a frequency count
            freq_dict.setdefault(value, 0)
            freq_dict[value] += 1
        elif operation == 2 and freq_dict.get(value):
            # delete AKA remove from frequencies
            freq_dict[value] -= 1
        elif operation == 3:
            if value in freq_dict.values():
                return_list.append(1)
            else:
                return_list.append(0)
            
    return return_list
