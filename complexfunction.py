def sum(list):
    sum = 1
    for l in list:
        sum = sum * l
    return sum

mylist = [1,2,3,4,5]
print(sum(mylist))