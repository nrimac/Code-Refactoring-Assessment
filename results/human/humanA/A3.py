# The function takes three parameters: price (float), discount_percent (float), and user_type (string) with either a value of "regular", "premium", or "vip".
# Example input: price=100.0, discount_percent=10.0, user_type="premium"

def calculate_discount(price, discount_percent, user_type):
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a positive number.")
        
    if not isinstance(discount_percent, (int, float)) or not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be a number between 0 and 100.")
    
    if not isinstance(user_type, str) or user_type.lower() not in {"regular", "premium", "vip"}:
        raise ValueError("User type must be one of: 'regular', 'premium', 'vip'.")
    
    user_type = user_type.lower()
    
    discount_amount = {"regular": 0, "premium": 1, "vip": 1.5}
    
    discount = discount_percent * discount_amount[user_type]
    discount = min(discount, 100.0)
    final_price = round(price * (1 - discount / 100), 2)
    
    return final_price

# Time to complete exercise: 
# 11:19 
