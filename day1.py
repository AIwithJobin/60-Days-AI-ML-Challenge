print("Hello world")

#variables in python
#what are variables ?
#variables are nothing but named containers which are used to store values of different types like string ,integer ,floating point ,
# etc .the values which are being stored can change..


x=50
print(x)

#data types refers to nothing but the different types of data which can be stored in avariable of a programming language

#python offers the following data types:
# int-- store integer values
# float--store numeric values which have a decimal point
#string --store sequences of ascii codes
# complex-- used to store complex values


print(type(x))

y=50.55
print(type(y))

y="python30"
print(type(y))

y="x"
print(type(y))

#complec data type
x=5+4j
print(type(x))
y=6+4j
print(x+y)

#strings,integers ,floating point values are all basic data types
#complex data types are derived data type,because it is ade up of integer data types or floating point data types or a combination
#  of both
#there are other data types offered by python which are used to store a collection of values in the place of a single value.
# again,they come under the derived data types


#list
# it is used to store a collection of values and these values are enclosed within a pair of square braces []

x=[1,2,2,4,5]#we can store values of different types in alist ..it is heterogeneous
print(type(x))
x=["dd",45,30.15,5+5j]
print(type(x))

#statically typed languages and dynamically typed
#in statically typed languages we need to mention the data type of the variable while declaring it .
# and we cant use the same variable to store values of different data types .

#int x=5
#.....
#x=34.4

#this cannot be done in c because it is statically types but in python we can do it
#languages which offers this flexibility is called dynamically typed languages

#tuples
#we  also use it to store a collection of values
#one difference in the syntax would be the way you declare and use tuples
# tuples are enclosed in parenthesis   '()'

x=(1,2,3,4,5,5)
print(type(x))

x=(1,12,512.64,"dfnjdsb",55+5j)
print(type(x))

x=[45,"Python",2+4j,3.12]#n list we can change the individual values
y=(1,2,3,"python",4.5615,3+4j)#but in tuples we can change the individual values
print(x[0])
print(x[2])
print(y[0])
print(y[4])

#string
sample="Python"
print(sample[1])
print(sample[0])

x[1]="py"
print(x)    #here the modification is done
# y[1]="opu"
# print(y)   #here it hows error because the modification cannot be done

# the technical term which are used to refer to this concept are "mutable" and "immutable".
#we cant new elements ,modify the values of tuples,nor we can concatenate 2 or more tuples or 
# we cannot delete any values from a tuple.
#all the above mentioned can be done in lists

x="python"
# x[1]='z'# this doed not work cannot point and change the values
#x= Python programming language
x=x+ "programmming language "#string can append values on either end ,in the front or in the back
print(x)
x="left concatenation "+ x
print(x)

#apart from the content which needs ro be displayed to the standard output,the print function also takes two optional arguments
#  which are "sep" and "end"
#"sep"-- seperator,, "end"-- endline

x="string1"
y="string2"
print(x,y)

#for any funtion the syntax is any thing in () are mandatory and anything inside[] are not mandatory they are optional
#print(Content,[])
print("c1","c2",sep=" ")
print("c1","c2",sep=",")
print("c1","c2",sep="random")


#end areguements
print("String1",end=":")
print("String2")


print("Strin1","String2",sep=":",end="::")
print("String3","String4")
print("String5","String6",sep=";")

# conditionals

#if conditional
#in senarios ,where you are supposed to execute a set of statements if acertain condition is true and noting otherwise,
# you will be using the if conditional

age=25
if(age>18):
    print("you are eligible for driving licence")
print("hi")

age=25
if(age>56):
    print("you are eligible for driving license")
print("hi")


#if else  condiitonal

age=25
if(age>18):
    print("you are eligible for driving licence")
else:
    print("you are not eligible for the driving licence")
print("hi")

#if else-if ...else  conditional

if(age>18):
    print("You are eligible for driving licence")
elif(age>=15):
    print("You are close to being eligible for having a licence")
else:
    print("you are still a child")

    # if (conditional):
    #     set of statements to be executed .
    #     rest of program


    # if(condition 1):
    #     set 1
    # else:
    #     set2
    # rest of program


    # if(condition1):
    #     set1
    # elif(condition2):
    #     set2
    # elif(condition 3):
    #     set3
    # ......
    # else:
    #     set 4
    # rest of program


mark=int(input("enter the mark"))

if(mark >= 90 ):
    print("O:Excellent")
elif(mark >=80 ):
    print("A:very good")
elif(mark >=70  ):
    print("B:good")
elif(mark>=60 ):
    print(" C: Average")
elif(mark>=50 ):
    print(" D:Below average")
else:
    print("F:Fail")

# formated strings in python

a="String1"
b="String2"
c=[1,2,3,4]
d=67
print("The value of a is ",a,"and the value of b is ",b,"but c is a list:",c,"and d is an integer",d)
#formated strings
print(f"the value of a is {a} and the value of b is {b} but c is alist:{c} and the avlue of d is an integer{d}")

mark=int(input("enter the mark"))

if(mark >= 90 ):
    grade ="O"
    comment="Excellent"

elif(mark >=80 ):
    garde="A"
    comment="very good"

elif(mark >=70  ):
    grade="B"
    comment ="good"

elif(mark>=60 ):
    grade="C"
    comment="average"

elif(mark>=50 ):
    grade="D"
    comment="below average"

else:
    grade="F"
    comment="fail"

print(f"The garde is {grade} and the comment is {comment}")

x=False
y=True
print(type(x))
print(x or y)
print(not x)

print(not(x or y))


# relational operators --- they are nothing but comparison operators
# theese are some of them :> , < , == ,>= ,<=,!=

# loops

# while loop:they are used to execute a particular block of code repeatedly until a certain condition is true

# while(condition):
#     set of statements to be executed

count= 1
while(count <=5):
    print(count)
    count+=1


count=1
while(count<=10):
    if(count==7):
        count+=1
        continue
    print(count)
    count+=1



x=int(input("Enter the integer"))
y=1
flag=0
while(y<=(x//2)):
    if(x%y==0):
        flag =1
        break
    y+=1
if(flag ==1):
    print("the number is a prime number")
else:
    print("the number is not  a prime number")

# write a program to take a non negative integer as your input and output the number of digits present in your input.
# use only while loop and no not use any in built function

x=int(input("enter the non negative integer"))

if(x<0):
    print("not possible")
if(x==0):
    print("number of digits int the input =1")
count=0
while(x>0):
    count += 1
    x=x//10

print(f"the number of digits in the input = {count}")



#write a program to take an positive integer as an input and print the first n number of the fibonacci numbers

num=int(input("Enter the positive integer"))
i=1
num1=0
num2=1
value=0
print(num1)
if(num2==1):
    print(num2)
while(i<=num-1):
    temp=num2
    num2=num2+num1
    print(num2)
    num1=temp
    i+=1


#write a program to take any integers as input and print weather n belongs to the fibonacci series or not and 
# if then it should also print the index of the number in the fibonacci series

num=int(input("Enter the integer"))
if(num<0):
     print("the number is not in the fibonacci series")
i=1
num1=0
num2=1
value=0
list=[0,1]
k=0
# print(num1)
# print(num2)
while(i<=num*2):
    temp=num2
    num2=num2+num1
    list.append(num2)
    num1=temp
    i+=1
print(list)

k=0
flag=0
while (k<(num*2)):
    if(num==list[k]):
        flag=1
        break
    k += 1

if(flag==1):
    print(f"the number is in the{k+1}th position ")
else:
    print("not in the fibonacci series")

##write a program which takes an non negative inter as an input and prints the first n odd numbers of the fibonacci series 
# along with the average of those n numbers

num=int(input("Enter the integer"))
check=num
if(num<0):
     print("please give a positive number ")
i=1
num1=0
num2=1
count=1
list=[1]
k=0
sum=1
# print(num1)
print(num2)
while(i<=num*num):
    temp=num2
    num2=num2+num1
    if(num2%2!=0):
        print(num2)
        list.append(num2)
        sum = sum + num2
        count+=1
        if(count==check):
            break
    num1=temp
    i+=1
print(list)
avg=sum/count
print(avg)