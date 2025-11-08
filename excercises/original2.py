# The function takes a list of dictionaries containing user information
# Example input: [{'name': "Alice", 'age': 32, 'email': "alice@example.com", 'score': 85}]

def process_user_data(data):
    result = []
    for i in range(len(data)):
        user = data[i]
        name = user['name']
        age = user['age']
        email = user['email']
        score = user['score']
        
        if age > 18:
            status = "adult"
        else:
            status = "minor"
            
        processed = {
            'username': name.upper(),
            'user_age': age,
            'user_email': email.lower(),
            'user_score': score * 1.1,
            'status': status
        }
        result.append(processed)
    
    return result

# Time to complete excercise: 
