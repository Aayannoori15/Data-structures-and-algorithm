def quick_sort(list1):
    pivot=list1[0]
    if len(list1)<=1:
        return list1
    else:
        lesser=[x for x in list1 if x<=pivot]
        higher=[x for x in list1 if x>pivot]
        return lesser+[pivot]+higher