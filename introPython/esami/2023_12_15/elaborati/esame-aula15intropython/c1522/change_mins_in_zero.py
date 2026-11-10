def change_mins_in_zero(values):
    minima= 0
    for i in range(len(values)-1):
        
        if values[i] <= values[i+1]:
            minima = values[i]

             
        else:
            minima = values[i+1]
    for i in range(len(values)-1):
        if values[i] <= minima:
            values[i]=0
   
            


list1 = [122,50,12,13,12,6,22,9]

print(list1)
change_mins_in_zero(list1)
print(list1)
      