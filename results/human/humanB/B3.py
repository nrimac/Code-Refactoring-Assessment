# The function takes three parameters: price (float), discount_percent (float), and user_type (string) with either a value of "regular", "premium", or "vip".
# Example input: price=100.0, discount_percent=10.0, user_type="premium"

def calculate_discount(price, discount_percent, user_type):
    if user_type == "premium":
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    elif user_type == "vip":
        discount = price * (discount_percent / 100) * 1.5  # VIPs get 50% more discount
        final_price = price - discount
        return final_price
    else:
        return price

def new_function(price, discount_percent, user_type):
    multiplier=1.0
    if user_type == 'vip':
        multiplier = 1.5
    elif user_type == 'premium':
        multiplier = 1
    else:
        return price
    discount=price*(discount_percent/100)*multiplier
    return price-discount

price=100.0
discount_percent=10.0
user_type="premium"
print(new_function(price, discount_percent, user_type))

# Time to complete excercise:

#6 min