# conditional statements: 

# rain -> umbrella
# sunny -> no umbrella

# mark >= 40: pass
# mark < 40: fail

# if statement:

# syntax:
"""
if condition :
    statement1

"""
# show if a user is eligible to vote or not, they can vote if their age is greater than or equals to 16
# age = 20
# address = "kathmandu"
# # python suite : indentation / tap
# # block 1
# if age >= 16: 
#      print("you can vote!!") # statement1
#      print("message1")
#      print("message2")
# # block 
# # 2
# if address == "kathmandu":
#      print("visit KMC, collect your voter id")
#      print("visit KMC, collect your voter id")
#      print("visit KMC, collect your voter id")
#      print("visit KMC, collect your voter id")
#      print("visit KMC, collect your voter id")
#      print("visit KMC, collect your voter id")

# print("thank you for checking your eligibility") # statement2



# if - else:

# syntax:
"""
if condition:
    statement1
else:
    statement2
"""

# age = int(input("enter your age:"))

# if age > 16:
#     print("you can vote!!")
# else:
#     print("you can't vote")


# number = int(input("enter any number: "))
# # number = int(number)

# if number%2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


# elif: 
# syntax:
"""
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
    .
    .
    .
    .

else:
    statement n
"""

# grading : A, B, C: AI model -> 90+ : A, 80+ B, 70+ C

# confidence_score = int(input("score: "))

# if confidence_score>= 90 and confidence_score<=100: #a- 90- 100
#     print("A")
# elif confidence_score>=80 and confidence_score<=90:  #b- 80-89
#     print("B")
# elif confidence_score>=70 and confidence_score<80:
#     print("C")
# else:
#     print("don't use this model")

# nested IF:
# syntax:
# if condition1:
#     if condition2:
#         statement1

# age = 20
# citizen = False

# if age >= 18:
#     if citizen == True:
#         print('you can vote!!')
#     else:
#         print('you can\'tvote')

# '  '  '
# "  ''  "

#escape character: 

"""
\n - new line
\\ - backslash
\t - tab
\' - single quote
\" - double quote
"""

# print("he said \"hello\'")

username = input('username: ')


if username == "binay":
                        password = input('password: ') 
                        if password == "12345":
                                    print('logged in successfull')
                                    x = int(input('passcode: '))
                                    if x == 1111:
                                        print('access granted')
                                    else:
                                        print('wrong passcode')
                        else:
                            print("wrong password")
else:
    print("register, you are not a user of this system")