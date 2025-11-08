# The function takes a list of dictionaries containing user information
# Example input: [{'name': "Alice", 'age': 32, 'email': "alice@example.com", 'score': 85}]

def process_user_data(data):
    result = []
    for i in range(len(data)):

        try:
            user = data[i]
            name = user['name']
            age = user['age']
            email = user['email']
            score = user['score']
        except Exception as e:
            print(f"Missing some information for user number {i+1}")
            continue

        
        if age > 18:
            status = "adult"
        else:
            status = "minor"
            
        processed = {
            'username': name.upper(),
            'user_age': age,
            'user_email': email.lower(),
            'user_score': round(score * 1.1, 2), # round to 2 decimals :)
            'status': status
        }
        result.append(processed)
    
    return result

# Time to complete excercise: 5min 20s
