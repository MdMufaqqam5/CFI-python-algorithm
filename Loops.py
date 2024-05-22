# # wap for 1 - 5 using for loop
print("wap for 1 - 5 using for loop")
for i in range(1,6):
    print(i)
print("-----------------------------")


# #wap for 1 - 5 using while loop
print("wap for 1 - 5 using while loop")
n = 1
while(n<6):
    print(n)
    n+=1
print("-----------------------------")


# # wap 5 - 1 using for loop
print("wap 5 - 1 using for loop")
for i in range(5,0,-1):
    print(i)
print("-----------------------------")


# # wap 5 - 1 using while loop
print("wap 5 - 1 using while loop")
n = 5
while(n>0):
    print(n*'*')
    n-=1
print("-----------------------------")


# #wap string using for loop
print("wap string using for loop")
a = "python"
for i in a:
    print(i)
print("-----------------------------")


# #wap string using while loop
print("wap string using while loop")
asd = "conda"
n = 0
while(n<len(asd)):
    print(asd[n])
    n+=1
print("-----------------------------")


# #wap all even numbers between 20-50 using while loop
print("wap all even numbers between 20-50 using while loop")
a = 20
while (a in range(20,51)):
    if ((a%2)== 0):
        print(a)
    a+=1
print("-----------------------------")


# #all even numbers between 20-50 method2 using while loop
print("all even numbers between 20-50 method2 using while loop")
a = 20
while(a in range(20,51)):
    print(a)
    a+=2
print("-----------------------------")


# # wap to all even numbers between 20-50 using for loop
print("wap to all even numbers between 20-50 using for loop")
for i in range(20,51,2):
    print(i)
print("-----------------------------")

#wap for sum of first 10 natural numbers using for loop
print("wap for sum of first 10 natural numbers using for loop")
sum = 0
for i in range(1,11):
    sum = sum+i
print(f"sum = {sum}")
print("-----------------------------")


#wap for sum of first 10 natural numbers using while loop
print("wap for sum of first 10 natural numbers using while loop")
sum = 0
i = 1
while(i<11):
    sum = sum+i
    i+=1
print(f"sum = {sum}")
print("-----------------------------")


#wap 10 - 2 using for loop
print("wap 10 - 2 using for loop")
for i in range(10,0,-2):
    print(i)
print("-----------------------------")


#wap 10 - 2 using while loop
print("wap 10 - 2 using while loop")
num = 10
while(num>0):
    print(num)
    num-=2
print("-----------------------------")


#wap to add all the values between u1-u2 using for loop
print("wap to add all the values between u1-u2 using for loop")
n1= int(input("enter the number: "))
n2= int(input("enter the number: "))
sum=0
for i in range(n1,n2+1):
    sum+=i
print(sum)
print("-----------------------------")


#wap to add all the values between u1-u2 using while loop
print("add all the values between u1-u2 using while loop")
n1= int(input("enter the number: "))
n2= int(input("enter the number: "))
sum=0
while(n1<n2+1):
    sum = sum+n1
    n1+=1
print(f"sum = {sum}")
print("-----------------------------")
