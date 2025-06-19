#condition
day_of_week= input("Enter the week : ").lower(); # convert lowercase
print(day_of_week)

if day_of_week =="sunday" or day_of_week =="wednesday":   #true
  print("I will learn python")
else: #false

 print("I wiil practice python")
  #-------------------------------------------------------------


Num1=int (input("Enter The first Number : ")); #input
Num2=int (input("Enter The second Number : "));

choice= input("Enter the operation : (Option +.,-,*,/,%) ")
if choice=="+":
    sum_of_num=Num1+Num2
    print("Addition :",sum_of_num)
elif choice=="-":
     diff_of_num=Num1-Num2
     print("subtrac ",diff_of_num)
elif choice=="*":
     prod_of_num=Num1*Num2
     print("product :",prod_of_num )
elif choice=="/":
     div_of_num=Num1/Num2
     print("division :",div_of_num)


elif choice=="%":
    rem_of_num=Num1%Num2
    print("remainder",rem_of_num)
else:
    print("Invalid choice") 
             
          

