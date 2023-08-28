def merge_sorted_lists(lista,listb):

    sortedlist = []

    i=0
    j=0

    while(i<len(lista)  and j<len(listb) ):

        if lista[i]<listb[j]:
            sortedlist.append(lista[i])
            i+=1
        else:
            sortedlist.append(listb[j])
            j+=1
    

    if i==len(lista) :
        sortedlist.extend(listb[j:])
        return sortedlist
    elif j==len(listb) :
        sortedlist.extend(lista[i:])
        return sortedlist

    return sortedlist
