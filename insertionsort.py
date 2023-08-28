def swap(mylist,posa,posb):
    temp = mylist[posa] #O(1)
    mylist[posa] = mylist[posb] #O(1)
    mylist[posb] = temp #O(1)

def insertionsort(mylist):
    len_list = len(mylist) #O(1)
    for i in range(1,len_list):
        for j in range(i,0,-1):
            if mylist[j]<mylist[j-1]:
                swap(mylist, j, j-1)

    return mylist

mylist=[99,4,2,6,5,1,3,44,9,23,78,11]
print(insertionsort(mylist))