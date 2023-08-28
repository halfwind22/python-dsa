def swap(mylist,posa,posb):
    temp = mylist[posa] #O(1)
    mylist[posa] = mylist[posb] #O(1)
    mylist[posb] = temp #O(1)

def selectionsort(mylist):
    len_list = len(mylist) #O(1)
    for i in range(0,len_list):
        min_index = i
        for j in range(i,len_list-1):
 #           print('Traversing J: ',j,' with outer iteration:',i)
            if mylist[min_index]>mylist[j+1]:
                min_index = (j+1)
        print('Mindex in interation: ',i,'is: ',min_index)
        if i!=min_index:
            swap(mylist, i, min_index)

    return mylist

mylist=[4,2,6,5,1,3,44,9,23,78,11]
print(selectionsort(mylist))