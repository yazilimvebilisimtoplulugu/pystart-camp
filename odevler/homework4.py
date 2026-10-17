directory={"Ali":"0555 111 22 33", "Ayşe": "0532 444 55 66"}
name=input("enter your name")
number=input("enter your phone number")
directory.update({
    name:number
})
directory["Ali"]= "0555 999 88 77"
del1= directory.pop("Ayşe")
print(del1)
name1=input("enter a name")
directory[name1]="No record founded"
print(directory[name1])