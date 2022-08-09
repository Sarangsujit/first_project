testing...............
# mul=1
# for i in range(1,11):
#     mul*=i
# print(mul)

num=12345
sum=0
for i in range(len(str(num))):  #convert num to string and find its length
    temp=num%10 #to get the last character
    num=num//10 #to avoid the last character
    # print(num)
    sum+=temp  #
print(sum)
