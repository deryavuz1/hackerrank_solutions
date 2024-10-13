
def matchingStrings(stringList, queries):
    len_queries = len(queries)

    results = [0] * len_queries
    
    for index, q in enumerate(queries):
        for elt in stringList:
            if elt == q:
                results[index] += 1
    
    return results
        
