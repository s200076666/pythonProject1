print("hello")
#print is function
#variables
x=20
print (x)
print("x")

text="hello ftaimah"
print(text)

f1="fatimah"
f1='fatimahh'
print(f1)
#CASE SENSETIVE
X=50
x=3
print(X)

num1=200
num2=100
num3=num1+num2
print(num3)

MYSTR1="hello"
MYSTR2=MYSTR1+" HANAN"
print(MYSTR2)

name= input("enter your name: ")
print("hello "+name)

numb1= input("enter the first number: ")
numb2= input("enter the second number: ")
result=float(numb1)+float(numb2) #بدونه يطبع الرقمين جنب بعض
print(result)

#list
MyList=["example","python","java",21,1,[1,3]]
print(MyList[2:])
print(MyList[0:3])
MyList [3]=12
print(MyList)

color=["red","pink","black","red"]
color2=["purple","blue"]
color2.append("green") #زياده في نهاية القائمه
color.insert(2,"white")
#color2.clear()
#color.remove()
#color.pop() #ازالة اخر عنصر

color += color2
print(color)

print(color.index("red")) #استعلام عن الوجود العنصر
print(color.count("red")) #كم مرا تواجد العنصر
print(color.sort())

#tuples
#ماينفع افير عليها
coordinate=(32,15)
print(coordinate)
list_of_tuples=[(1,2),(3,4),(5,6)]
print(list_of_tuples)

#function
 #def say_hi():
     #print("hello fatimah") #المسافه تعرفني اني داخل الدالة
#print(first)
    #say_hi()

def say_hi(name,age):
    Print("hello "+name+ " your age is "+str(age))
    print(say_hi("fatimah",23))

def cube(nu1,nu2):
    return nu1*nu2
print(cube(3,6))

#condition
def match_string(str1,str2):
    if str1 == str2 : #!=
        print("string match")
    else :
        print("string dont match")

match_string("fatimah","hanan")

#calclator
n1= float(input("enter first number: "))
operator= input("enert the operator: ")
n1= float(input("enter second number: "))

if operator == "+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)
elif operator == "+":
    print(n1 * n2)
elif operator == "*":
    print(n1+n2)
elif operator == "/":
    print(n1/n2)
else:
    print("wrong operator please try again")

#dictionaries stores data "key": "value"
convvert_month = {
    aug: augast,
    feb: feburary,
    jun:june }
print(convvert_month.get('feb'))

# while loop
i=1
while i<=10 :
    i += 1
    if i==6:
        continue
        #break
    print(i)
print( 'loop has eneded')

#for loop
for letter in "fatimah":
    print(letter)

color3=["grren","blue","pink"]
for x in color3:
    print(x)

for x in range(5):
    print(x)

for index in range(10):
    if index % 2 ==0:
        print(index, " is even number")
    else:
      print(index, " is odd number")


