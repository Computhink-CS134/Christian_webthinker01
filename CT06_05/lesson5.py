print("Hello from lesson 5")
user = input("Enter your name: ")
age = input ("what is your age this year")
message = input("what would you like to tell him/her?")

print("happy" + age + "th birthday, " + user + "! " + "btw," + message)

for i in range(5):
    print("hi")

for i in range(100):
    print("i like nasi padang")

for i in range(100):
        print("i like cake")
        print("give me more")
# loop starts with 0

for count in range(1,11,1):
    print(count)

#for count in range(start,stop,step)

# when start,when stop,how many to skip 

#e.g if step is 2, it will skip 1 number 1,3,5 etc
#if step is 3 it will skip 2 numbers 1,4,7 etc
#if you dont put step it will automatically be 1

# #if step is negative, it will count backwards by that number
#e.g range(10,0,-1) will count backwards from 10 to 1
#e.g range(20,10,-2) will count backwards from 20 to 12, skipping 1 number each time
#note that it will stop before reaching 0

#   |
#   v   can be anything(its a var)e.g count, i, num,rfeg,gere,regre,anything basically
for count in range(0,60):
        print(count)

for count in range(1,6):
      print(count)

for count in range(51,101):
    print(count)

for count in range(18,30):
     print(count)

for i in range(2,25,2):
    print(i)

for i in range(8,97,8):
    print (i)

for i in range(5,0,-1):
    print(i)

for i in range(100,-1,-2):
    print(i)

for i in range(0,101,3):
    print(i)

name=input("what is your name?")
for i in name:
     print("give me a " + i)
print("what do we have?")
print(name + " is the best!")


print("ready!")
for i in range(3,0,-1):
    print(i)

for i in range(10,0,-1):
    print(i)
if(i==1):
   print("BOO")
#== -> comparison operator (checks if both sides are equal)
#= -> assignment operator (assigns value on right to variable on left)

num=0
for i in range(10):
     #num =num + i
     num =num + 1
     print(num)

var1=input("enter first number:")
var2=input("enter second number:")
for i in range int(var1,var2+1):
    print(i) 
