#basic
for i in range(0,50,1):
    print(i)

#Multiples of 5
for i in range(5,100000000,5):
    print(i)

#Counting, the Dojo Way
for i in range(0,101,1):
    if i%5==0:
        if i%10==0:
            print("Dojo")
        else:
            print("Coding")
    else:
        print (i)

#woah that sucker's huge
x=0
for i in range(1,500000,2):
    x+=i
print(x)

#countdown by fours
for i in range(2018,0,-4):
    print(i)

#flexible countdown
def flexCD( lowNum, highNum, mult):
    for i in range(highNum,lowNum,mult):
        print(i)

#outputs
#3,5,1,2
#not an int
#prints a list the size of list