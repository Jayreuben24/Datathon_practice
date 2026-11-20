## Problem 2.1 — The Automated Student Grade Processor 

## imports libraries
import numpy as np

## inputs number of grades and grades

## input validation for the number of grades
while True:
    try:
        n = int(input("Please enter the number of grades: "))
    except ValueError:
        print("Please input a valid number.")
        continue
    if n <=0:
        print("Please enter a number greater than zero.")
        continue
    break

## input validation for the grades
def get_grades(text):
    while True:
        try:
            grade = float(input(text))
        except ValueError:
            print('Please input a valid score.')
            continue
        if grade < 0 or grade > 100:
            print('Please enter a valid score (0-100).')
            continue
        break
    return grade

## for loop for grades inputs base on the number of samples
grades = []
for i in range(n):
    score = get_grades(f'Please input the score for test {i+1}: ')
    grades.append(score)
    
grades = np.array(grades)
meanGrade = np.mean(grades)

## grade classification logic
def classification(score):
    if score >=90:
        return ("Excellent")
    elif score >=80 and score <90:
        return ("Very Good")
    elif score >=75 and score <80:
        return ("Passed")
    else:
        return ("Failed!")

## Output : Classified Grades  
gradeClassified ={}
for i, value in enumerate(grades):
    gradeClassified[f'Exam{i+1}']=classification(value)
    print (f'Exam No. {i+1} : {value:.2f} is {gradeClassified[f'Exam{i+1}']}')
    
print(f'The Average of {n} Exams is {meanGrade} which is {classification(meanGrade)}.')