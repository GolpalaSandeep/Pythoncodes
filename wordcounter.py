def wordcounter(string):
    for char in string:
        if char not in arr:
            arr.append(char)
    for char in arr:
        for i in string:
            if (i==char):
                
