# The function takes three parameters: price (float), discount_percent (float), and user_type (string) with either a value of "regular", "premium", or "vip".
# Example input: price=100.0, discount_percent=10.0, user_type="premium"

def calculate_discount(price, discount_percent, user_type):
    """
    Calculates the final price after applying a discount based on the user type.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The percentage of the discount.
        user_type (str): The type of user ("regular", "premium", or "vip").

    Returns:
        float: The final price after the discount is applied. Returns the
               original price if the inputs are invalid.
    """
    if not all(isinstance(arg, (int, float)) for arg in [price, discount_percent]):
        return price
        
    if not isinstance(user_type, str):
        return price

    if price < 0 or not 0 <= discount_percent <= 100:
        return price

    discount_multipliers = {
        "regular": 0.0,
        "premium": 1.0,
        "vip": 1.5
    }

    user_type_lower = user_type.lower()
    if user_type_lower not in discount_multipliers:
        return price

    multiplier = discount_multipliers[user_type_lower]
    
    discount = price * (discount_percent / 100) * multiplier
    final_price = price - discount
    
    return final_price

# Time to complete excercise: 9''