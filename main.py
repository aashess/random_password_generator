import random

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

number=['0','1','2','3','4','5','6','7','8','9']

symbol=['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator")

letter_input=int(input("How many letters do you like in your password?\n"))

symbol_input=int(input("How many symbols do you like?\n"))

number_input=int(input("How many numbers do you like?\n")) 

password_list =[]

for char in range(1,letter_input+1):
    password_list.append(random.choice(letter))
for charr in range(1,number_input+1):
    password_list.append(random.choice(number))
for charrr in range(1,symbol_input+1):
    password_list.append(random.choice(symbol))

random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your password: {password}")

# password=""
# for charrrr in password_list:
#     password+=charrrr

# print(f"Your password: {password}")



