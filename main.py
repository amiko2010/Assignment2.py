from functools import wraps


SYSTEM_ACTIVE = True
GLOBAL_AUDIT_LOG = []


def audit_system(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
       
        if SYSTEM_ACTIVE:
            GLOBAL_AUDIT_LOG.append(f"გამოიძახა ფუნქცია: {func.__name__} (args: {args}, kwargs: {kwargs})")
        return func(*args, **kwargs)
    return wrapper



def create_account_generator(initial_balance):
    balance = initial_balance
    transaction_id = 0
    
   
    @audit_system
    def account_gen():
        nonlocal balance, transaction_id
        while True:
           
            amount = yield (transaction_id, balance)
            if amount is not None:
                balance += amount
                transaction_id += 1
                
    return account_gen()