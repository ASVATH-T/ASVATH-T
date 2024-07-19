def grading_students(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            rounded_grades.append(grade + (5 - (grade % 5)))
        else:
            rounded_grades.append(grade)
    return rounded_grades

if _name_ == "_main_":
    grades = [84, 29, 57]
    print(grading_students(grades))
