inventory = {
    "laptop": {
        "price": 2500,
        "stock": 5,
        "release_year": 2024
    },
    "smartphone": {
        "price": 1800,
        "stock": 12,
        "release_year": 2025
    },
    "headphones": {
        "price": 300,
        "stock": 20,
        "release_year": 2023
    },
    "tablet": {
        "price": 1200,
        "stock": 8,
        "release_year": 2024
    }
}


name = str(input("Enter name of product: ")).strip().lower()

if name in inventory:
    
    inventory[name]["stock"] = int(input("Enter new stock: "))
    
else:
    
    inventory[name] = {
        "price": float(input("price: ")),
        "stock": int(input("stock: ")),
        "release_year": int(input("realease_year: "))
    }
    

active_users = {"nino@gmail.com", "giooo", "luka12", "mariami"}
vip_users = {"giooo", "mariami", "dato_g"}


all_users = active_users.union(vip_users)



active_vips  = active_users.intersection(vip_users)



non_vip_active = active_users.difference(vip_users)



for name, products in inventory.items():
    if products["stock"] > 0:
        print(f"{name}: {products['stock']} \n")

most_expensive = ""
max_price = 0

for name, products in inventory.items():
    if products["price"] > max_price:
        max_price = products["price"]
        most_expensive = name

print("most expensive product: ", most_expensive)


total_value = 0
for name, info in inventory.items():
    total_value = products["price"] * products["stock"]
     

    print(f"{name}: price - {products['price']}, stock - {products['stock']}, release_year - {products['release_year']},total_value  - {total_value }\n")


print(f"all_users : {all_users }\n")
print(f" active_vips: { active_vips}\n")
print(f"non_vip_active: {non_vip_active}\n")