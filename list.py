change_list=[1,2,3,4,5,"Hello","Job",True,False,None,[1,2,3,4,5,6,7,8,9,10]]
print(change_list)
change_list[0]="Change1"
print(change_list)
change_list[-1]="Change_Last"
print(change_list)
change_list[0:3]=["Hello"]  #[0:3] do not include the 3rd position
print(change_list)
change_list.insert(4,"sarang")
print(change_list)
change_list.append("append")
print(change_list)   #change last value ,opposite of -1