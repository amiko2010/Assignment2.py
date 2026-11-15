

class Product:
    """ონლაინ მაღაზიის ერთი პროდუქტი."""

   
    store_name = "TechShop Georgia"
    currency = "GEL"
    total_products = 0          

   
    def __init__(self, name, price, stock, category, discount=0):
       
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.discount = discount        

        
        Product.total_products += 1

 
    def get_info(self):
        """აბრუნებს სტრიქონს პროდუქტის სრული ინფორმაციით."""
        return (f"პროდუქტი: {self.name} | "
                f"ფასი: {self.price} {Product.currency} | "
                f"მარაგი: {self.stock} ც. | "
                f"კატეგორია: {self.category} | "
                f"ფასდაკლება: {self.discount}%")

    def apply_discount(self, percent):
        """ცვლის ფასდაკლებას მითითებულ პროცენტზე და ბეჭდავს შეტყობინებას."""
        
        if percent < 0 or percent > 100:
            print(f"შეცდომა: ფასდაკლება უნდა იყოს 0-დან 100-მდე (მიიღეთ {percent}).")
            return
        self.discount = percent
        print(f"{self.name}: ახალი ფასდაკლებაა {self.discount}%")

    def update_stock(self, amount):
        """მარაგს ამატებს (amount > 0) ან აკლებს (amount < 0)."""
        new_stock = self.stock + amount

        if new_stock < 0:
           
            print(f"გაფრთხილება: {self.name}-ის მარაგი არ არის საკმარისი! "
                  f"გვაქვს {self.stock} ც., მოთხოვნილია {-amount} ც.")
            return

        self.stock = new_stock
        print(f"{self.name}: მარაგი განახლდა, ახლა არის {self.stock} ც.")

    def calculate_final_price(self):
        """აბრუნებს საბოლოო ფასს ფასდაკლების გათვალისწინებით."""
        final_price = self.price - (self.price * self.discount / 100)
        return round(final_price, 2)    

    
    @classmethod
    def get_total_products_count(cls):
        """აბრუნებს, სულ რამდენი პროდუქტია შექმნილი."""
        
        return cls.total_products






if __name__ == "__main__":
   
    p1 = Product("Smartphone X", 1200, 15, "Electronics")
    p2 = Product("Wireless Headphones", 250, 30, "Electronics", discount=10)
    p3 = Product("Running Shoes", 180, 8, "Sportswear")

    print("--- get_info ---")
    print(p1.get_info())
    print(p2.get_info())
    print(p3.get_info())

    print("\n--- apply_discount + calculate_final_price ---")
    p1.apply_discount(15)
    print(f"საბოლოო ფასი ფასდაკლებით: {p1.calculate_final_price()} {Product.currency}")
    print(f"{p2.name}: {p2.calculate_final_price()} {Product.currency}")
    p3.apply_discount(150)         

    print("\n--- update_stock ---")
    p3.update_stock(5)             
    p3.update_stock(-2)             
    p3.update_stock(-100)           

    print("\n--- კლასის მეთოდი ---")
    print(f"სულ შექმნილი პროდუქტები: {Product.get_total_products_count()}")
    print(f"მაღაზია: {Product.store_name}")