def calculte_grade(student_score):
    if student_score >= 70:
        return "A"
    elif student_score >= 60:
        return "B"
    elif student_score >= 50:
        return "C"
    elif student_score >= 45:
        return "D"
    else:
        return "F"

student_name=input("Enter student name: ")
stdent_score=int(input("Enter student score: "))

grade=calculte_grade(stdent_score)

print("\n--- Student Results ---")
print("Name: ", student_name)
print("Score: ", grade)