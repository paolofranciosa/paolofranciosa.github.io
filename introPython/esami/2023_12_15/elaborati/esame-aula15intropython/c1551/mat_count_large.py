def mat_count_large(m, threshold):
    count=0
    for x in m:
        for i in x:
            if i>threshold:
                count+=1
    return count
          
            