def linearsearch(list1, e):
    for i in range(len(list1)):
        if list1[i] == e:
            return i
    return None