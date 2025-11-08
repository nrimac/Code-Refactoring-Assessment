# The function takes a list of dictionaries containing student names and their scores,
# Example input: [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}, {'name': 'Charlie', 'score': 78}]

def calculate_average_scores(scores):

    if(len(scores)==0):
        return []

    total = 0
    count = 0
    
    for student in scores:
        total += student['score']
        count += 1
    
    average = total / count
    
    above_average = []
    for student in scores:
        if student['score'] > average:
            above_average.append(student['name'])
    
    return above_average


# Time to complete excercise: 2min 30s
