#age = 12
#if (age >= 18):
 #   print("you are an adult")
#else:
#    print("you are not an adult")

#if (age<18):
 #   print("you are not an adult")
#if (age>=13):
 #       print("you are a teenager")
#elif (age<65):
 #   print("you are an adult")
#else:
 #   print("you are a senior citizen")

Student=0
while(Student<=5):

    marks = int(input("please enter your marks: "))

    if(marks>=70):
        print("A")

    elif(marks>=55):
        print("B")

    elif(marks>=40):
        print("C")
    else:
        print("F")
    Student+=1

 