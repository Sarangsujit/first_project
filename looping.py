# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(i)
#

# list=[1,2,3,4,5,6,7,8,9,10]
#
#
# odd_list=[1,3,5,7,9]
# even_list=[2,4,6,8,10]
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

# num = int (input (“Enter any number to test whether it is odd or even: “)
# if (num % 2) == 0:
#     print (“The number is even”)
#else: print

list=[1,2,3,4,5,6,7,8,9,10]
odd_list=[]
even_list=[]

for i in list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(odd_list)
print(even_list)
