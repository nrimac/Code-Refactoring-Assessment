# The function takes a list of dictionaries containing student names and their scores,
# Example input: [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 90}, {'name': 'Charlie', 'score': 78}]

def calculate_average_scores(scores):
    """
    Calculates the average score from a list of student dictionaries and 
    returns a list of names of students who scored above the average.

    This refactored function includes comprehensive data validation and edge case
    handling to prevent exceptions and ensure stable execution. It improves 
    readability by using list comprehensions.
    """

    # 1. Input validation: Use a guard clause to check if the input is a list.
    # This prevents TypeErrors if a non-list is passed.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQExnHTmbULEJ5Y0seU84pmCpOP2qjUZCozEs0gypoT7pnfn008PBTZCsDuev3Am0241xtIalYNxmg-ditsXgrk8TcKB9h9sL9o6RPo1-9OmnL32hDrr90rQ0KmvIU2SqSjHUmL9BKgx1yRXxhu6oeWLrJZb)]
    if not isinstance(scores, list):
        return []

    # 2. Data Sanitization: Filter the list to include only valid student entries.
    # A valid entry is a dictionary containing a 'name' and a numeric 'score'.
    # This prevents KeyErrors for missing keys and TypeErrors for non-numeric scores.
    # Using a list comprehension is a concise and readable "Pythonic" approach.[[2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGSFy3Cul1jIL-hZMwzqvBW1Sizc-8moBfia0AxHojmJpqhYPHmlGp1UL3tY9n_1m3qOCuzOV4gJ0mmHInxR7tgQ4lUOC2zDyExyMzROypddP7gUkwXFZGwoE5rj4-oPShnAMhxJtC2G0YDvFjZgFIMKwECL1cXMlRTlZKyNrazkuJP649lAdJm)][[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFrbMze-8D54QCxVCSRWpabv1ujzrMr8PgW4g5VLB1_2zU1_KPH7Xsu0ZmaiaUQv3Jxlk7etrEOKHCJYv2-ue8OcCr6x8nCEnUAgsTf75CCy2zYVaXSkcIzHvOTylPRzfvllXgUSjHbiz6gKySElhGiGP2zIPbN1tPtqTU%3D)][[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHtYz_eJuxUFFpnFtlYmH31PSR2Y7O4nJtdMTCIAlkL1G_Kxg0hHN528YVjZc9HHzliAHaz03DE9_aX2i6Y8v8vhyteupQRctUmbCFmvy5A_ngDxxPCqoTQwXDq_u6Y0Dj-Uan1aFGheosUWqADjelNrYZi-iF0X5HNrLmw9vGUsx4q98hl_AyF8XMOfJt_vaiUS265RpraHHxTFpE%3D)]
    valid_students = [
        student for student in scores
        if isinstance(student, dict) and
           'name' in student and
           'score' in student and
           isinstance(student.get('score'), (int, float))
    ]

    # 3. Edge Case Handling: Check if there are any valid students to process.
    # If the list is empty after filtering, division by zero would occur.[[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHJgiuq6YDSOQruIpBjiXbJMm4KhJA2F3qy46qaE30321oLJgCGyb0SIpvtNHN5u_Lv-fChdZFZYNgySIQE7FBGsq3pZZe2zEOnbyFjAF8ijheVJS2R5bEDayEfMQifR4uesXQ1d7ZSZ_j7w4D_A6LnXt6_dbClQbxN55wY9AQjsBaZqi650LNqpsx6ZQypHRH1UA%3D%3D)][[6](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFGD9OVr8A7OiOZCIZw-w8oqIrSc-EtaHL_X2bRzh4u6dPzU2jK2Ujene0rN0EXxk5VI7eaJrI-o94rpBrBhpod57QEYIvK7P-33I_8iZJqpoxVeGAiL-Ixg8AsjzdZ6vFLNNwu_wEDNRRkAH1fA6-Ga7vJ1wyqmiJ6jxmB4UOH7w%3D%3D)]
    # Returning early avoids the ZeroDivisionError.
    if not valid_students:
        return []

    # 4. Calculation: Compute the average score from the sanitized data.
    # A generator expression within sum() is efficient for this calculation.[[7](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQF5KhUtFmu-MwUupR9w-o-DdJqcz7stPCalyOlqonejvBeTHY65MEScMEWkyv5T-hO30e4g6fPH4kHdcTrjCqY5k88LLjnIm9fZ2oddsth6CVr84uxZXxrInqpEPDios-lgTfs57ptjynLm-yDtWJfoHxnGesyJrG_h30G0WgvZhr3gfEU6Yy_8iAbbLZZL8nGTBDkrYM6pJcoHkn0MiEXP9-FLMsak)][[8](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFWnf8UJ16Gk6dXZcGLufYTzVmYs5DM933l0pvlSv7rB1jumOKbWnhw5nON9w5drQPzf8edntKc7DQww-0FBd-kN20JDHpP7WQ04LOhOAYEFIbxp8sjRvGdqXrrGv_7-t7EzTQuaiGoPAWlJh9fTOP9j6N42IWLFgYVg_l1O4SrOb00OiEZNUGNPvbJPN-v97KZTykPa28%3D)]
    total_score = sum(student['score'] for student in valid_students)
    average_score = total_score / len(valid_students)

    # 5. Result Generation: Use a final list comprehension to find students
    # who scored above the calculated average. This is more readable than a manual loop.[[9](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHQXbre2IZnY-B8PnIsgQ9pByZ-eU889adY0-CA1yUhVBpfzr6nZq7K_S4OyH-ZAMBHbCxzI-C33LSUXwC5G3L1-kl3ymjQgjP9pv6euegbe1-OsfePOgC0_b_fplIcKRm1upStjlBo7rwbyoVUSFIs9NT_H7hbdpXjA4sKKZodLg%3D%3D)]
    above_average = [
        student['name'] for student in valid_students 
        if student['score'] > average_score
    ]
    
    return above_average

# Time to complete excercise: 20''