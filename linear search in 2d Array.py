#Question:store random values in a 2d array with 4 rows and 2 columns(of name and age) then take imput the name user want to search perform linear search if found greet user and diplay his age else if not found print ann appropriate message
Array=[["Alishba Anwar",18],["Taha Anwar",18],["Hiba Anwar",27],["Taha Ali",32]]
def LinearSearch(array,nametosearch):
    count=0
    valuefound=False
    notinlist=False
    while valuefound==False and notinlist==False:
        if array[count][0]==nametosearch:
            valuefound=True
            return count
        else:
            count=count+1
        if count>3:
            notinlist==True
            return -1
for x in range(3):
    name=input("Please enter the name you want to search: ")
    temp=LinearSearch(Array,name)
    if temp==-1:
        print("The name was found on array")
    else:
        print("Assalam u Alaikum,",Array[temp][0]+"\n"+"Your age is,",Array[temp][1])


