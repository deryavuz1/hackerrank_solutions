def runningMedian(a):

    int_list = []
    median = 0
    toReturn = []
    
    for index, elt in enumerate(a):
        #int_list.append(elt)
        bisect.insort(int_list, elt)
    
        if len(int_list) % 2 == 0:
            mid1 = len(int_list) / 2
            mid2 = int(mid1) - 1
            median = (int_list[int(mid1)] + int_list[mid2])/2
        elif len(int_list) % 2 != 0:
            index = math.floor(len(int_list)/2)
            median = int_list[int(index)]
    
        toReturn.append("{:.1f}".format(median))
    return toReturn
