#მომხმარებლის ინფორმაცია
user_name = input("What is your name?\n").upper()

user_surname = input("What is your surname?\n").upper()

user_birthyear = input("What is your birthyear?\n")

user_fpl = input("What is your favourite programing language?\n")

now = 2026

user_age= now - int(user_birthyear)

is_adult = user_age >= 18

print(user_name,user_surname,user_birthyear ,user_fpl,is_adult,sep=" | ")


#მოსწავლის ნიშანი

score = input("Enter your score (max 20 points): ")


grade =int(score // 2)


print("your grade is ", grade)

