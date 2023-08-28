from mergesort import merge_sorted_lists

def recursive_splitter(mylist):

    if len(mylist)==1:
        return mylist
    else:
        return merge_sorted_lists(recursive_splitter(mylist[:int(len(mylist)/2)]),
        recursive_splitter(mylist[int(len(mylist)/2):]))

mylist=[99,4,2,6,5,1,3]
print(recursive_splitter(mylist=mylist))