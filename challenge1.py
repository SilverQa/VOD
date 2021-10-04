# password = "opensesame"
# if len(password) < 8:
#     print("Password too short, try again.")
# else:
#     print("Password accepted")

# score = 0
# num = input("Gimme a number now! ")
# num = int(num)
# if (num % 7 == 0) and (num % 3 == 0):
#     print(f"{num} is FIZZBUZZ - 100 points!")
#     score += 100
# elif num % 3 == 0:
#     print(f"{num} is fizz - 5 points!")
#     score += 5
# elif num % 7 == 0:
#     print(f"{num} is buzz - 10 point!")
#     score +=10
# else:
#     print(f"{num} is not fizz OR buzz. You get no points for that.")
# print(f"You scored {score} at the end. Well done!")

# word = input("Please enter a word \n")

# first = word[0]
# len = len(word)
# last = word[len-1]

# if last == first:
#     print("True")
# else:
#     print("False")

# num1 = 23
# num2 = 43

# num1 = int(input("can pls make number?\n"))
# num2 = int(input("choose another one\n"))

# sum = num1 + num2
# if sum % 2 == 0:
#     print("the sum is EVEN ayyyyyyyy")
# else:
#     print("number is not even u LOSER")

word = "ziggy"
length = len(word)
x = 0
while x < length/2:
   print(word[x],word[length-x-1])
   x = x + 1


