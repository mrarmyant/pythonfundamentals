#biggie size
def bSize(arr):
    for i in range(0,len(arr),1):
        if arr[i] > 0:
            arr[i]="big"
    return arr

#countpositives
def cPos(arr):
    x=0;
    for i in range(0,len(arr),1):
        if arr[i]>0:
            x+=1
    arr[len(arr)-1]=x
    return arr

#sumtotal
def sTot(arr):
    total=0;
    for i in range(0,len(arr),1):
        total+=arr[i]
    return total

#average
def avg(arr):
    total=0
    for i in range(0,len(arr),1):
        total+=arr[i]
    return total/len(arr)

#length
def leng(arr):
    return len(arr)

#minimum
def mini(arr):
    minim=arr[0];
    if leng(arr)==0:
        return False
    for i in range(1,leng(arr),1):
        if minim>arr[i]:
            minim=arr[i]
    return minim

#maximum
def maxi(arr):
    maxim=arr[0];
    if leng(arr)==0:
        return False
    for i in range(1,leng(arr),1):
        if maxim<arr[i]:
            maxim=arr[i]
    return maxim

#ultimate analyze
def ultim(arr):
    released = {
        "sumTotal": sTot(arr),
        "maximum":maxi(arr),
        "minimum": mini(arr),
        "average" : avg(arr),
        "length": leng(arr)
    }
    return released

#reverselist
def reverse(arr):
    y=arr.length
    swap = ""
    for i in range(0,y,1):
        swap=arr[i]
        arr[i]=arr[y]
        arr[y]=swap
        y-=1
    return arr
