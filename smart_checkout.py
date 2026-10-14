
cart_total =  0

user_status = "vip"

has_promo_code = True

loyalty_points = 500

delivery_city = "თბილისი"

is_account_active = True

discount = 0


if is_account_active == False:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდება.")

else:
    if cart_total <= 0:
        print("შეცდომა")
    else:
           

        if user_status =="vip":
            discount = 20
            if loyalty_points >= 500:
               discount = 25
        elif user_status =="regular":
            if has_promo_code == True or cart_total >= 150:
               discount = 10 
        elif user_status =="admin":
                    discount = 50

price_after_disc = cart_total - (cart_total * discount / 100)

if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
    if price_after_disc >= 100:
            delivery = 0
    else :
        delivery = 5
else:
    delivery = 15

 
total = int(price_after_disc + delivery)   

print(cart_total,discount,delivery,total)
 



