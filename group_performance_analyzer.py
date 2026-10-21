

scores = []

while True:
    user_input = input("შეიყვანეთ ქულები (0-10) ან 'stop' დასრულებისთვის: ")
    
    
    if user_input== "stop":
        break
   
    
    parts = user_input.split()
    
   
    for part in parts:
        try:
            score = int(part)
            
            
            if 0 <= score <= 10:
                scores.append(score) 
            else:
                print("გაფრთხილება: ქულა უნდა იყოს 0-სა და 10-ს შორის.")
                
        except ValueError:
            
            print("გთხოვთ შეიყვანოთ სწორი რიცხვი ან 'stop'")


print("\n")
if len(scores) > 0:
    min_score = min(scores)
    max_score = max(scores)
    avg_score = sum(scores) / len(scores)
    
   
    print(f"მინიმალური ქულა: {min_score}")
    print(f"მაქსიმალური ქულა: {max_score}")
    print(f"კლასის საშუალო ქულა: {avg_score:.2f}")
    
    sorted_scores = sorted(scores)
    print(f"ყველა ქულა ზრდადობით: {sorted_scores}")
    
    
    print("ქულების გამეორებები:")
    for s in sorted(set(sorted_scores)):
        count = scores.count(s)
        print(f"  - ქულა {s}: გამეორდა {count}-ჯერ")
