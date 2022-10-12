# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
# ⦁	2.00 – 2.99 - "Fail"
# ⦁	3.00 – 3.49 - "Poor"
# ⦁	3.50 – 4.49 - "Good"
# ⦁	4.50 – 5.49 - "Very Good"
# ⦁	5.50 – 6.00 - "Excellent"
#

def grade_in_words(some_grate):

    if 2 <= some_grate <= 2.99:
        return "Fail"
    elif 3.00 <= some_grate <= 3.49:
        return "Poor"
    elif 3.50 <= some_grate <= 4.49:
        return "Good"
    elif 4.50 <= some_grate <= 5.49:
        return "Very Good"
    elif 5.50 <= some_grate <= 6.00:
        return "Excellent"


received_grade = float(input())
result = grade_in_words(received_grade)
print(result)
