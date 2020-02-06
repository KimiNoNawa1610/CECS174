#Nhan Vo
# Part 2 Problem 5:
my_dict=dict(milk=0, candy=-1, book=100)
for key, value in my_dict.items():
    if value<0:
        my_dict[key]=0
print(my_dict)
