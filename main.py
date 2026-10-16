import re

ticket_price = 15

user_text = input("შეიყვანეთ ტექსტი: (მაგ: Minda 3cali bileti, gadavixade 60 lari)\n")

numbers = re.findall(r"-?\d+",user_text )

try:
    tickets_amount = int(numbers[0])
    paid_amount = float(numbers[1])

  
    if tickets_amount <= 0:
     raise ValueError("ბილეთების რაოდენობა უნდა იყოს მინიმუმ 1")
    
    total_cost = tickets_amount * ticket_price

    if paid_amount < total_cost:
     raise ValueError("თანხა არ არის საკმარისი")
    
except (IndexError, ValueError) as e:
  
  print(f"შეცდომა: {e}")

else:

  change = paid_amount - total_cost
  print(f"ჯავშანი წარმატებულია! ხურდა: {change:.2f} ლარი")

finally:
  print("სისტემა: ტრანზაქციის მცდელობა დასრულდა.")