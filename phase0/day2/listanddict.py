##we are now working with lists.
i=0
list=[]
while(True):
    choice=input("Add elements? (y/n)")
    if choice=="y":
        print("Enter ",i," element:")
        element=int(input())
        list.append(element)
    elif choice=="n":
        break
    else:
        print("Invalid Choice.")
    i=i+1
##printing list
i=0
print("List:")
for i in range(0,len(list)):
    print(list[i])


##another way
user_input=(input("Enter student marks seperated by white spaces")).split()
sum=0
for i in range(len(user_input)):
    sum+=int(user_input[i])
print("Average marks are:",sum/len(user_input))