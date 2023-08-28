def swap(mylist,posa,posb):
    temp = mylist[posa] #O(1)
    mylist[posa] = mylist[posb] #O(1)
    mylist[posb] = temp #O(1)

def insertionsort(mylist):
    len_list = len(mylist) #O(1)
    for i in range(1,len_list):
        start=mylist[i]
        previous=i-1
        print("Starrt: ",start)
        while start<mylist[previous] and previous>-1:
            #Comparison is always between adjacent values.
            #previous+1 is actually start here.
            swap(mylist, previous+1, previous)
            print("After swapping: ",mylist," iteration: ",i,"and previous is ",previous)
            previous-=1

    return mylist

mylist=[99,4,2,6,5,1,3]
print(insertionsort(mylist))
#44,9,23,78,11,99