students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

#Average student marks
def calculate_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)
    return average

print(calculate_average([78, 85, 90]))

#performance categorization

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

print(classify_performance(84.33))

#Student report

def display_report(students):
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        average = calculate_average(marks)
        performance = classify_performance(average)

        print("ID:", student_id)
        print("Name:", name)
        print("Average:", average)
        print("Performance:", performance)



display_report(students)



