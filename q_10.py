newlist1=[]
list1 = [10, 20, 25, 30, 35]
for x in list1:
    if x % 2 == 0:
        newlist1.append(x)
print("newlist1:",newlist1)

newlist2=[]
list2=[40,45,60,75,90]
for x in list2:
    if x % 2 == 0:
        newlist2.append(x)
print("newlist2:",newlist2)
merge=newlist1 + newlist2
print("merge_list:",merge)
