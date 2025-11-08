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
def new_process(data):
    result = []
    for user in data:
        status = 'adult' if user['user_age'] > 18 else 'minor'
        processed = {
            'username': user['username'].upper(),
            'user_age': user['user_age'],
            'user_score': user['user_score']*1.1,
            'status': status,
            'user_email': user['user_email'].toLower()
        }
        return result.append(processed)

data=[
    {'name': "Alice", 'age': 32, 'email': "alice@example.com", 'score': 85}
]
print(process_user_data(data))
# Time to complete excercise:

#8 min