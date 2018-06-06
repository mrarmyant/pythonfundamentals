#countdown
def cDown(num):
    arrOut = []
    for i in range (num,-1,-1):
        arrOut.append(i)
    print (arrOut)
    return arrOut

#print and return
def pRet(num1,num2):
    print(num1)
    return(num2)

#firstpluslength
def fstLen(arr):
    return arr[0]+len(arr)

#valuesgreatersecond
def bigSecong(arr):
    if len(arr)<=1:
        return False
    newArr =[]
    counter=0
    bigNum = arr[0]
    for i in range(0,len(arr),1):
        if arr[i]>arr[1]:
            count+=1
            newArr.append(arr[i])
    print (count)
    return newArr

#Thislengththatvalue
def lenVal(num1,num2):
    arr=[]
    if num1==num2:
        print ("Jinx!")
    for i in range(0,num1,1):
        arr.append(num2)
    return arr




