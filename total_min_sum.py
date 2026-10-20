total = 0
count = 0
max_num = 0
min_num = 0

while True:
    user_input = input("შეიყვანეთ რიცხვები (ან 'stop' დასრულებისთვის): ")
    

    if user_input.strip().lower() == "stop":
        break


    parts = user_input.split()
        
   
    for part in parts:
        try:
            
            num = float(part)
            
            
            total += num
            count += 1

            if   num > max_num:
                 max_num = num
            if  num < min_num :
                   min_num = num


        except ValueError:
         print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი ან 'stop'") 
        

