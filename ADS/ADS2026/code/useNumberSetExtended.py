from numModuleExtended import Number_set

a = Number_set()   # create an object of class Number_set
b = Number_set()   # create another object of class Number_set
print(b.get_avg()) # object "b", executes its "get_avg" function
a.add(10)          # object "a", executes its "add" function       
a.add(100)         # object "a", executes its "add" function
b.add(-56)         # object "b", executes its "add" function
b.add(-4)          # object "b", executes its "add" function
print("a max", a.get_max())
print("a min", a.get_min())
print("a average", a.get_avg())
print("b nums", b.get_num())
print("b max", b.get_max())
print("a contains max", a.get_num_negative(), "negatives and ", a.get_num_positive(), "positives")
print("b contains max", b.get_num_negative(), "negatives and ", b.get_num_positive(), "positives")

var = b.get_variance()
print("b's variance is", var)
