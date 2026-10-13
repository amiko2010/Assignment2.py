#ავტომატური ელფოსტის გენერატორი

user_name=input("Enter your name:\n").strip().lower()

user_surname=input("Enter your surname:\n").strip().lower()

domain=input("Enter your preffered domain (for example: gmail.com, itstep.ge, yahoo.com):\n")

user_name1=(user_name[0:2])

at_sign="@"

formated_email=f"{user_name1}{user_surname}{at_sign}{domain}"

print(formated_email,end="\n\n")

print("თქვენი ელფოსტა წარმატებით შეიქმნა!")