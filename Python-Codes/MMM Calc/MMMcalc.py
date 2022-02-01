import statistics as stat

list1 = [ 22, 13, 28, 13, 22, 25, 7, 13, 25 ]

list_mean=stat.mean(list1)
list_median=stat.median(list1)
list_mode=stat.mode(list1)

print("Given List :", list1)

print("Mean :", list_mean)
print("Median :", list_median)
print("Mode :", list_mode)