def swap(mylist,posa,posb):
    temp = mylist[posa] #O(1)
    mylist[posa] = mylist[posb] #O(1)
    mylist[posb] = temp #O(1)

def bubblesort(mylist):
    len_list = len(mylist) #O(1)
    for i in range(1,len_list-1):
        for j in range(0,(len_list)-i):
            print('Traversing J: ',j,' with outer iteration:',i)
            if mylist[j]>mylist[j+1]:
                swap(mylist, j, j+1)

    return mylist

mylist=[4,2,6,5,1,3]
print(bubblesort(mylist))