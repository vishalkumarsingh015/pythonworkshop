#Lsit -> ordered sequence of different type of values 

#how to define a list?
#user=['raj','sham','rajesh']

# List How to get values from a list?


# users[0], users[1],users[-1]

user_list=['Alex','Ram','Sham','Aki']
print(user_list)

print(user_list[0])
print(user_list[-1])

#adding item to a list
# user.append('vishal')
user_list.append('vishu')

print(user_list)
 #How to delete values form a list?
 #user.remove('raju')

user_list.remove('vishu')
print(user_list)


#How to modify values from a list?
#users[1]="shan"
user_list[1]='vishal'
print(user_list)


#adding item to a list at given position?
#user.insert(1,'shanu')
user_list.insert(2,'shanu')
print(user_list)

#How to delete values form a list using index no
#del users[2]
del user_list[4]
print(user_list)

#length of list
#len(users)

print(len(user_list))

#sorting the items in list?
#users.sort()
#users.sort(reverse=True)
#users.reverse()
user_list.sort(reverse=True)
print(user_list)

user_list.reverse()
print(user_list)

#popping the items in list? remove last value
user_list.pop()
print(user_list)

remove_value=user_list.pop(1)
print(remove_value)


# suers_list=['alok','raju','sham','Bhola']
# print(suers_list[0:2])


marks=[89,90,100,45,33,56]
print(marks)

print(min(marks))
print(max(marks))
print(sum(marks))




