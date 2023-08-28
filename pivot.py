def swap(mylist,posa,posb):
    temp = mylist[posa] #O(1)
    mylist[posa] = mylist[posb] #O(1)
    mylist[posb] = temp #O(1)

def pivot(mylist,start_index,end_index):
    swap_ptr=pivot=start_index

    for i in range(start_index+1,end_index+1):
        if mylist[pivot]>mylist[i]:
            swap_ptr+=1
            swap(mylist,swap_ptr,i)

    swap(mylist, swap_ptr, pivot)
    return swap_ptr

# mylist=[4,2,6,5,1,3]
# print(pivot(mylist, 0,5))
# print(mylist)
# print(pivot(mylist, 0,2))
# print(mylist)
# print(pivot(mylist, 4,5))
# print(mylist)