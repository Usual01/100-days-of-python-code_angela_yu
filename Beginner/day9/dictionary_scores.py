"""
write a program that converts their scores to grades in a dictionary_student grades
their names for keys and grades for values
create an 
"""
student_scores  = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 90,
    "Draco": 74,
    "Neville": 62,
}

new_dict = {}
for student in student_scores:
    scores =student_scores[student]
    if scores >= 90:
        new_dict[student] = "outstanding"
    elif scores >= 80:
        new_dict[student] = "exceeds expectation"
    elif scores >= 70:
        new_dict[student] = "acceptable"
    else:
        new_dict[student] = "fail "
print(new_dict)