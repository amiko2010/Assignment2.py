class BankAccount:
    bank_name = "BOG" 
    account_count = 0  

    def __init__(self, card_type: str, owner: str, initial_balance: float = 0.0):
        self.card_type = card_type
        self.owner = owner
        self._min_balance = 0.0  
        self.__balance = 0.0     
        self.balance = initial_balance  
        BankAccount.account_count += 1

   
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < self._min_balance:
            raise ValueError(f"შეცდომა: ბალანსი ვერ იქნება {self._min_balance}-ზე ნაკლები!")
        self.__balance = value

    @balance.deleter
    def balance(self):
        print(f"ანგარიშის მფლობელ {self.owner}-ის ბალანსი განულდა და წაიშალა.")
        self.__balance = 0.0

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("შეტანილი თანხა უნდა იყოს 0-ზე მეტი.")
        self.balance += amount  
        print(f"[Deposit] {amount} ლარი წარმატებით ჩაირიცხა. მიმდინარე ბალანსი: {self.balance} ლარი.")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("მოსახსნელი თანხა უნდა იყოს 0-ზე მეტი.")
        if amount > self.balance:
            raise ValueError("ანგარიშზე არ არის საკმარისი თანხა.")
        self.balance -= amount
        print(f"[Withdraw] მოხსნილია {amount} ლარი. მიმდინარე ბალანსი: {self.balance} ლარი.")

    @classmethod
    def update_bank_name(cls, new_name: str):
        cls.bank_name = new_name
        print(f"ბანკის სახელი შეიცვალა და გახდა: {cls.bank_name}")

    @classmethod
    def get_total_accounts(cls):
        return f"ბანკში ({cls.bank_name}) სულ შექმნილია {cls.account_count} ანგარიში."

    @staticmethod
    def calculate_tax(amount: float) -> float:
        
        return amount * 0.20


class SavingsAccount(BankAccount):
    def __init__(self, card_type: str, owner: str, initial_balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(card_type, owner, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"[Savings] დაერიცხა საპროცენტო სარგებელი: {interest} ლარი.")

   
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("მოსახსნელი თანხა უნდა იყოს 0-ზე მეტი.")
        commission = amount * 0.01
        total_deduction = amount + commission
        
        if total_deduction > self.balance:
            raise ValueError("არ არის საკმარისი თანხა საკომისიოს (1%) ჩათვლით.")
        
        self.balance -= total_deduction
        print(f"[Savings Withdraw] მოხსნილია {amount} ლარი (საკომისიო: {commission}). მიმდინარე ბალანსი: {self.balance} ლარი.")


class CreditAccount(BankAccount):
    def __init__(self, card_type: str, owner: str, initial_balance: float = 0.0, credit_limit: float = 2000.0):
        super().__init__(card_type, owner, initial_balance)
        self.credit_limit = credit_limit
        self._min_balance = -self.credit_limit 

 
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("მოსახსნელი თანხა უნდა იყოს 0-ზე მეტი.")
        
       
        if (self.balance - amount) < -self.credit_limit:
            raise ValueError(f"ოპერაცია ვერ შესრულდა: გადააჭარბეთ საკრედიტო ლიმიტს ({self.credit_limit} ლარი).")
        
        self.balance -= amount
        print(f"[Credit Withdraw] მოხსნილია {amount} ლარი. მიმდინარე ბალანსი: {self.balance} ლარი.")