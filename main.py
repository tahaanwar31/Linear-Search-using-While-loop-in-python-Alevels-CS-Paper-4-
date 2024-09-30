arraydata=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def LinearSearch(searchvalue,array):
    flag=False
    count=0
    while flag==False:
        if arraydata[count]==searchvalue:
            flag=True
            return count
        count=count+1
        if count>len(arraydata)-1:
            flag=True
            return-1
number=int(input("Please enter the number you want to search: "))
result=LinearSearch(number,arraydata)
if result!=-1:
    print("The number was found on",result,"position")
else:
    print("The number was not found in the array")