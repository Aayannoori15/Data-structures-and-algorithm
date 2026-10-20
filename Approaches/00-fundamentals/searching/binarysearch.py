def binarysearch(list1,l,h,e):
    mid = (l+h)//2
    while l<=h:
        if e==list1[mid]:
            return mid 
        if e<list1[mid]:
            binarysearch(list1,l,mid-1,e)
        else:
            binarysearch(list1,mid+1,h,e)
    return None