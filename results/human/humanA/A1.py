# The function takes a list of dictionaries containing student names and their scores,
# Example input: [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}, {'name': 'Charlie', 'score': 78}]


def calculate_average_scores(scores):
    if not isinstance(scores, list):
        raise ValueError("Scores must be a list.")
        
    for student in scores:
        if not isinstance(student, dict):
            raise ValueError("Student data must be a dictionary.")
        if not isinstance(student['score'], int):
            raise ValueError("Student score must be an integer.")
        if not isinstance(student['name'], str):
            raise ValueError("Student name must be a string.")
    
    average = sum(student['score'] for student in scores) / len(scores)
    above_average = [student['name'] for student in scores if student['score'] > average]
    
    return above_average

# Time to complete exercise: 
# 13:55
