# The function takes three parameters: price (float), discount_percent (float), and user_type (string) with either a value of "regular", "premium", or "vip".
# Example input: price=100.0, discount_percent=10.0, user_type="premium"

def calculate_discount(price, discount_percent, user_type):

    if not isinstance(price, float):
        raise Exception("price should be float")
    if not isinstance(discount_percent, float):
        raise Exception("discount_percent should be float")
    if not isinstance(user_type, str):
        raise Exception("user_type should be a string")
    if discount_percent > 100:
        raise Exception("discount_percent cannot be bigger than 100")

    if user_type == "premium":
        discount = price * (discount_percent / 100)
        return price - discount
        
    elif user_type == "vip":
        discount = price * (discount_percent / 100) * 1.5  # VIPs get 50% more discount
        return price - discount
        
    else:
        return price

# Time to complete excercise: 8 min 
