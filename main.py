#1

def factorial_recursive(n):     
    #   შევქმენთ ფუნქცია factorial_recursive() არგუმენტით n,რომელიც ითვლის რიცხვის ფაქტორიალს რეკურსიული მეთოდით
    if n < 0:
        return "Factorial is not defined for negative numbers."
    #   ფუნქცია ამოწმებს არგუმენტს,თუ ის ნაკლებია ნულზე აბრუნებს წინადადებას, რომელიც გვეუბნება, რომ ფაქტორიალი არ განისაზღვრება უარყოფით რიცხვებზე

    if n == 0 or n == 1:
        return 1
     #   საბაზისო შემთხვევა: თუ არგუმენტი ტოლია 0ის ან 1ის, მისი ფაქტორიალი იღებს 1ის ტოლ მნიშვნელობას,პროგრამა აბრუნებს 1ს (ციკლი სრულდება)
    
    return n * factorial_recursive(n - 1)
      #   პროგრამა აბრუნებს არგუმენტისა და არგუმენტს-1 ის ფაქტორიალის ერთმანეთზე გადამრავლებისას მიღებულ მნიშვნელობას,რაც შესაბამისად არგუმენტის ფაქტორიალის ტოლია

# ფუნქცია საბოლოო პასუხს იგებს შემდეგნაირად, თავდაპირველად ფუნქცია ჩადის საბაზისო შემთხვევამდე, მაგალითად: factorial_recursive(5) ის შემთხვევაში პირველ რიგში კომპიუტერი იხმობს factorial_recursive(5)ს, რაც უდრის 4 x factorial_recursive(4) , შემდეგ factorial_recursive(4)ს მანამ სანამ არ ჩავა factorial_recursive(1)მდე, რომლის მნიშვნელობაც იცის რომ ერთია,ამის შემდეგ ამოდის ისევ უკან და მიდის საბოლოო პასუხამდე (5 x factorial_recursive(4)= 5 x 24 = 120)


      
   



#2

def calculate_cart_total(discount_rate, *prices):
  
  discount_multiplier = 1 - (discount_rate / 100)

  total = 0 
  for price in prices:  
    discounted_price = price * discount_multiplier  
    total += discounted_price 

  return float(total)

def filter_and_sort_products(**products):
  
  filtered_items = filter(lambda item: item[1] >= 100, products.items())

  
  sorted_products = sorted(filtered_items, key = lambda item: item[1])


  return list(sorted_products)


#3

from functools import reduce
 

names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]

def pair_students(names_list, scores_list):
   student = list(zip(names_list, scores_list))
   return student

paired_students = pair_students(names,scores)



def get_passed_students(paired_data, passing_score=60):
   passed_students=list(map(lambda student : student[0], list(filter(lambda paired_data : paired_data[1]>=passing_score,paired_data))))
   return passed_students



import functools

def calculate_average_of_passed(passed_students):
  scores_only = list(map(lambda item: item[1], passed_students))

 
  total_sum = functools.reduce(lambda x, y: x + y, scores_only)

 
  return total_sum / len(passed_students)



