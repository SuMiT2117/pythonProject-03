import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("Welcome to the password Generator !")

n_letter = int(input(f"How many letters you want to include in the password ?\n"))
n_numbers = int(input(f"How many numbers you want to include in the password ?\n"))
n_symbols = int(input(f"How many symbols you want to include in the password ?\n "))
#easy level:

#password =""

#for char in range(0,n_letter):
#    password += random.choice(letters)

#for char in range(0 , n_numbers):
#    password += random.choice(numbers)

#for char in range(0 , n_symbols):
#    password += random.choice(symbols)

#print(password)

#hard level:
password_list =[]
password =""

for char in range(0,n_letter):
    password_list.append(random.choice(letters))

for char in range(0 , n_numbers):
    password_list.append(random.choice(numbers))

for char in range(0 , n_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is : {password}")