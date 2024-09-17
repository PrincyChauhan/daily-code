def have_common_substring(s1,s2):
    set1=set(s1)
    print("set1....",set1)
    set2=set(s2)
    print("set2....",set2)
    
    if set1 & set2:
        return True
    else:
        return False
    