#Reading inputs
n = int(raw_input())
arr = [[raw_input(),float(raw_input())] for x in xrange(0,n)]
#print arr

#find smallest element and filter it out from list
min_1 = min(arr, key=lambda x: x[1])
arr =filter(lambda a: a[1] != min_1[1], arr)

#Find second smallest elemant
min_2 = min(arr, key=lambda x: x[1])
#print min_2[1]

#creating a new list with condition
newList = []
for item in arr:
    if min_2[1] in item:
        newList.append(item[0])
        
newList = sorted(newList)
print '\n'.join(newList)
