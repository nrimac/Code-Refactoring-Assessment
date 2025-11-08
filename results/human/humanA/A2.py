# The function takes a list of dictionaries containing user information
# Example input: [{'name': 'Alice', 'age': 32, 'email': 'alice@example.com', 'score': 85}]

def process_user_data(data):
    if not isinstance(data, list):
        raise ValueError("Users information must be a list.")
    
    result = []
    for user in data:
        if not isinstance(user, dict):
            raise ValueError("User information must be a dictionary.")
        
        required_keys = {'name', 'age', 'email', 'score'}
        missing_keys = required_keys - user.keys()
        if missing_keys:
            raise ValueError(f"User is missing one or more required keys.")

        name = user['name']
        age = user['age']
        email = user['email']
        score = user['score']
        
        if not isinstance(name, str):
            raise ValueError(f"User name must be a string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError(f"User age must be a non-negative integer.")
        if not isinstance(email, str) or '@' not in email or '.' not in email:
            raise ValueError(f"User email must be a valid email address.")
        if not isinstance(score, (int, float)):
            raise ValueError(f"User score must be numeric.")
        
        status = "adult" if age > 18 else "minor"
            
        processed = {
            'username': name.strip().upper(),
            'user_age': int(age),
            'user_email': email.strip().lower(),
            'user_score': round(score * 1.1, 2),
            'status': status
        }
        result.append(processed)
    
    return result

# Time to complete exercise: 
# 10:47
