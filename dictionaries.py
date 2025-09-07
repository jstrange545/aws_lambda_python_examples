# Nested dictionary

student_grades = {
    "John": {
        "Math": {
            "Assignments": [90, 85, 77],
            "Exams": [88, 76]
        },
        "Science": {
            "Assignments": [92, 89],
            "Exams": [84, 77]
        },
        "English": {
            "Assignments": [85, 82, 94],
            "Exams": [90]
        }
    }
}

print(student_grades["John"]["Math"]["Exams"]) #Output should be [88, 76]

# A general example

payload = {
    "Avariable": {
        "ProgramConfigOne": 1,
        "ProgramConfigTwo": 1
    }
}

print(payload)
print(payload["Avariable"]["ProgramConfigOne"])

# looping through keys and values

for key in student_grades.keys():
    print(key)

for value in student_grades.values():
    print(value)

for key, value in student_grades.items():
    print(f"{key}: {value}")