# 
marks={'Hindi':98,'Enligh':89}
print(marks)
print(type(marks))
print(marks['Hindi'])
#new add subject with marks

marks['Math']=99
print(marks)

#How to delete values from a dictionary?

del marks['Hindi']
print(marks)
 

 #Getting no. of key-value a Dictionary?
length= len(marks)
print(length)