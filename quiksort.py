from pivot import pivot

def quicksort(mylist,start_index,end_index):
    if start_index<end_index:
        
        pivot_index = pivot(mylist, start_index, end_index)
        print("pivot is at: ",pivot_index)
        quicksort(mylist=mylist,start_index=start_index,end_index=pivot_index-1)
        quicksort(mylist=mylist,start_index=pivot_index+1,end_index=end_index)


mylist=[4,2,6,5,1,3]
print(quicksort(mylist, 0,5))
print(mylist)
        