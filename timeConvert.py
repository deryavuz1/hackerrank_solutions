def timeConversion(s):
    
    split_arr = s.split(":")
    hour = split_arr[0]
    new_hour = 0.0
    new_last = 0.0
    
    if "PM" in split_arr[2]:
        if int(hour) != 12:
            new_hour = 12 + int(hour)
        else:
            new_hour = 12
        new_last = split_arr[2].removesuffix("PM")   
    elif "AM" in split_arr[2]:
        if int(hour) != 12:
            new_hour = int(hour)
        else:
            new_hour = "00"
        new_last = split_arr[2].removesuffix("AM")
    
    new_time = str(new_hour) + ":" + str(split_arr[1]) + ":" + str(new_last)
    return new_time
