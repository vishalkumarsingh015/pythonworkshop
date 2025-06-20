#loop concept
#data structer which can hold multiple values of multiple type

list_of_Cloud = ["aws","Azure","Gcp","Alibaba Claoud"]
list_of_Cloud.append("sleceforce")
list_of_Cloud.append("IBM")
print(list_of_Cloud)

# -> new cloud add "append" 


list_of_Cloud.insert(2,"ICP")
print(list_of_Cloud)

list_of_Cloud.insert(0,"BCP")
print(list_of_Cloud)


#iteration of a list
for cloud in list_of_Cloud:
  print(",")
  print(cloud)

  #range 
  for i in range(0,11):
     print(i)

