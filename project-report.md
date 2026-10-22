# PYTHON APPLICATION PROJECT REPORT

## Student Grade Calculator

**Submitted By:** Om More  
**Roll Number:** 10  
**College:** Pimpri Chinchwad University (PCU)  
**Department:** Artificial Intelligence and Machine Learning (AIML)  
**Subject:** Python Programming  
**Project Title:** Student Grade Calculator  

---

## 1. Introduction

The Student Grade Calculator is a simple Python-based application designed to calculate student marks, average percentage, grades, and results automatically.

Python is one of the most popular programming languages because of its simple syntax and wide range of applications. It is commonly used in software development, artificial intelligence, machine learning, and data analysis.

The main purpose of this project is to demonstrate basic Python programming concepts through a practical application.

The application allows users to enter student details and marks in three subjects. It calculates the total marks, average percentage, and final grade based on predefined conditions.

This project helps beginners understand how Python can automate mathematical calculations and improve accuracy.

## 2. Problem Statement

Calculating student marks manually can be time-consuming and may result in calculation errors.

Educational institutions need accurate methods to calculate student performance.

The Student Grade Calculator solves this problem by providing an automated system that calculates marks and displays results.

The application reduces manual calculations and improves efficiency.

## 3. Objectives

The main objectives of this project are:

1. To develop a simple Python application.
2. To understand Python programming fundamentals.
3. To accept input from users.
4. To calculate total marks and average percentage.
5. To assign grades using conditional statements.
6. To display student results automatically.
7. To understand functions, loops, and dictionaries.
8. To upload and manage Python projects using GitHub.

## 4. Software and Hardware Requirements

### Software Requirements

- Programming Language: Python 3
- Code Editor: Visual Studio Code or Python IDLE
- Version Control Platform: GitHub
- Operating System: Windows, Linux, or macOS

### Hardware Requirements

- Computer or laptop
- Minimum 2 GB RAM
- Basic processor
- Keyboard and monitor

No additional Python libraries are required.

## 5. System Design

The Student Grade Calculator follows a simple input-processing-output model.

### Input

The application accepts:

- Student name
- Python marks
- Mathematics marks
- Computer Science marks

### Processing

The program performs the following calculations:

**Total Marks = Python + Mathematics + Computer Science**

**Average Percentage = Total Marks / 3**

The application then assigns a grade according to the average percentage.

### Output

The program displays:

- Student name
- Subject-wise marks
- Total marks
- Average percentage
- Grade
- Final result

## 6. Algorithm

**Step 1:** Start the program.

**Step 2:** Display the application title.

**Step 3:** Accept the student's name.

**Step 4:** Accept marks for three subjects.

**Step 5:** Validate the entered marks.

**Step 6:** Calculate the total marks.

**Step 7:** Calculate the average percentage.

**Step 8:** Assign a grade using conditional statements.

**Step 9:** Determine the pass or improvement status.

**Step 10:** Display the final student report.

**Step 11:** Stop the program.

## 7. Python Concepts Used

### Variables

Variables store information such as student names, marks, totals, and averages.

### Input and Output

The `input()` function accepts user information, while the `print()` function displays results.

### Conditional Statements

The application uses `if`, `elif`, and `else` to assign grades and determine the final result.

### Loops

A `for` loop is used to collect marks for different subjects. A `while` loop repeats input requests when invalid marks are entered.

### Functions

Functions divide the program into smaller, reusable parts.

The application uses:

- `get_mark()` to accept and validate marks.
- `calculate_grade()` to determine grades.
- `main()` to control the application.

### Dictionaries

A Python dictionary stores subject names and their corresponding marks.

### Exception Handling

The program uses `try` and `except` to handle invalid numeric input.

## 8. Grade Calculation System

The application uses the following grading criteria:

| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

The student receives PASS status when the average is at least 40% and every subject mark is at least 35.

Otherwise, the program displays NEEDS IMPROVEMENT.

These grading criteria are examples for this project.

## 9. Sample Input and Output

### Sample Input

Student Name: Om More

Python Marks: 80

Mathematics Marks: 90

Computer Science Marks: 70

### Sample Output

```text
STUDENT GRADE CALCULATOR

----- STUDENT REPORT -----

Student: Om More

Python : 80.0
Mathematics : 90.0
Computer Science : 70.0

Total: 240.0 / 300
Average: 80.0 %
Grade: A
Result: PASS
```

### Explanation

The application adds all three subject marks.

Total = 80 + 90 + 70 = 240

Average = 240 / 3 = 80%

According to the grading conditions, an average of 80% receives grade A.

Since the student satisfies the passing requirements, the result is PASS.

## 10. Testing

The following test cases can be used to verify the application:

| Test Case | Input | Expected Output |
|---|---|---|
| Normal marks | 80, 90, 70 | Grade A, PASS |
| Low marks | 20, 30, 40 | Grade F, NEEDS IMPROVEMENT |
| Full marks | 100, 100, 100 | Grade A+, PASS |
| Invalid marks | 120 | Ask for valid marks |
| Invalid text | abc | Display input error |

Testing helps identify errors and verify the accuracy of calculations.

## 11. Advantages

The advantages of this application include:

1. Easy to understand and use.
2. Simple Python implementation.
3. Automatic calculation of marks.
4. Reduced manual calculation errors.
5. Basic input validation.
6. No external libraries required.
7. Suitable for beginners learning Python.

## 12. Limitations

The application has a few limitations:

1. It processes one student at a time.
2. It supports only three predefined subjects.
3. Student information is not permanently stored.
4. It does not provide a graphical user interface.
5. Grading conditions are predefined.

These limitations can be addressed in future versions.

## 13. Future Scope

The application can be improved by adding advanced features.

Possible improvements include:

- Support for multiple students.
- Database integration using MySQL.
- Saving results in CSV or Excel format.
- A graphical user interface using Tkinter.
- Automatic report generation.
- Customisable grading rules.
- Web application development using Flask.

These improvements would make the application more useful for educational institutions.

## 14. GitHub Repository

GitHub is a platform used by developers to store, manage, and share source code.

The Student Grade Calculator project has been uploaded to GitHub.

**Repository Name:** student-grade-calculator

**Repository Link:**

https://github.com/ommore1042008-hub/student-grade-calculator

The repository contains the Python source code and project documentation.

GitHub also provides version control, which helps developers manage changes to their projects.

## 15. Conclusion

The Student Grade Calculator is a beginner-friendly Python application that demonstrates important programming concepts.

The project uses variables, functions, loops, dictionaries, conditional statements, exception handling, and mathematical operations.

It automatically calculates student marks, averages, grades, and results.

Developing this project provides practical experience in Python programming and helps improve logical thinking and problem-solving skills.

The project also introduces GitHub as a platform for managing and sharing software projects.

Overall, the Student Grade Calculator demonstrates how simple Python programs can automate routine tasks and provide accurate results.

---

**Submitted By:** Om More  
**Roll No.:** 10  
**College:** Pimpri Chinchwad University  
**Department:** AIML  
**Project:** Student Grade Calculator
