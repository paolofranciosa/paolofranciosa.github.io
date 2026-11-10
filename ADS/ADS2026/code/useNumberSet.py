from numModule import Number_set

a = Number_set()   # create an object of class Number_set
b = Number_set()   # create another object of class Number_set
print(b.get_avg()) # object "b", executes its "get_avg" function
a.add(10)          # object "a", executes its "add" function       
a.add(100)         # object "a", executes its "add" function
b.add(-56)         # object "b", executes its "add" function
b.add(-4)          # object "b", executes its "add" function
print("a max", a.get_max())
print("a average", a.get_avg())
print("b nums", b.get_num())
print("b max", b.get_max())

###########################################################
#         add here the following calls                    #
# and modify the Number_set class definition accordingly  #
###########################################################

# print("the number of negative inserted elements in b is", b.get_negatives())
# var_a = a.get_variance()
# print("a's variance is", var_a)
#
# var_b = b.get_variance()
# print("b's variance is", var_b)
