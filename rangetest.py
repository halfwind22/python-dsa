mylist=[4,2,6,5,1,7]
len_list = len(mylist)
print(int(len_list/2))
for i in range(1,len_list):
    for j in range(i,0,-1):
        print("interation : ",i,"Value= ",j)
    print