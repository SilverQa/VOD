import datetime as date
qa = date.datetime.now().year - date.datetime(1968,4,20).year
print(qa)
print(date.datetime.now().year)

# age = input("What is your age?")
# age = int(age)
# usa = input("Do you live in the USA? yes/no ")

# if age > 20 and usa == "yes":
#     print("Yes I can serve you")
# elif age > 17 and usa == "no":
#     print("Yes I can serve you")
# else:
#     print("You are not old enough!")


age = input("What is your age?")
age = int(age)
usa = input("Do you live in the USA? yes/no ")

if age < 18:
    print("NO")
elif age < 21 and usa == "yes":
    print("NO")
else:
    print("YES!!")

