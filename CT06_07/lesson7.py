
#can only concatanate SAME TYPES(FLOAT,INTEGER,STRING) CHANGE WITH -  (FLOAT/INT/STR(x))
print("lesson 7 ACTUAL")

#TYPES OF ERRORS:NAME,TYPE,VALUE,INDEX,SYNTAX,KEY
#NAME ERROR: when you try to use a variable that has not been defined
#TYPE ERROR: when you try to perform an operation on a variable that is not the correct type
#VALUE ERROR: when you try to perform an operation on a variable that has the correct type but the value is not valid
#INDEX ERROR: when you try to access an index that is out of range
#SYNTAX ERROR: when you try to write code that is not valid python syntax
#KEY ERROR: when you try to access a key that does not exist in a dictionary


sum=0
for i in range(5):
    n=input ("say number #" + str(i)+":")
    sum= int(n) +sum
print(sum)

n=input ("what number to multiply?: ")
for i in range(1,13):
    print(str(n) + " x " + str(i) + " = " + str(int(n)*i))

for i in range(1,6):
    n+input("say a number" + str(i)+ "=")
    sum + int(n) +sum
print (sum)