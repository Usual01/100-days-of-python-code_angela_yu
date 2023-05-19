import random
names = ["dami", "tobi", "moyo", "kemi", "afe", "sina", "miracle"]
student_sscores = {student:random.randint(45, 100) for student in names}
passed = {student:score for (student,score) in student_sscores.items() if score >= 60}
print (student_sscores)
print(passed)