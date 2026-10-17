name=input("enter name")
department=input(" enter your department")
age=int(input("enter your year of birth"))
age1=int(input("enter your birthday"))
age2=int(input("enter your year birth mount"))
name=name.title()
tuple=(age1, age2, age)
year=2026 - age
print("name and surname :", name)
print("department :",department)
print(f"born :{tuple[0]:02d}.{tuple[1]:02d}.{tuple[2]}")

print("age :",year)