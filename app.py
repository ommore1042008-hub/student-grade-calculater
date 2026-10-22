
def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def main():
    print("STUDENT GRADE CALCULATOR")
    name = input("Enter student name: ")

    subjects = ["Python", "Mathematics", "Computer Science"]
    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    total = sum(marks.values())
    average = total / len(subjects)

    result = (
        "PASS"
        if average >= 40 and all(mark >= 35 for mark in marks.values())
        else "NEEDS IMPROVEMENT"
    )

    print("\n----- STUDENT REPORT -----")
    print("Student:", name)

    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("Total:", total, "/ 300")
    print("Average:", round(average, 2), "%")
    print("Grade:", calculate_grade(average))
    print("Result:", result)


if __name__ == "__main__":
    main()
