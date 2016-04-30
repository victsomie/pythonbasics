lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#Function on main average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)

#function to calculate individual averages
def get_average(student):
    homework=average(student["homework"])
    quizzes=average(student["quizzes"])
    tests=average(student["tests"])
    return (homework*0.1) + (quizzes*0.3) + (tests*0.6)

#Create the test score
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

#Call the get_letter_grade method with llyd's results
get_letter_grade(get_average(lloyd))

#The average for the whole class
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

students = [lloyd, alice, tyler]#Creates students list
print get_class_average(students) #print the class average
print get_letter_grade(get_class_average(students)) #Prints the grade of the class based on the average of the class

"""
Functions and Lists
Passing a range into a function
Okay! Range time. The Python range()function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.


range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
The range function has three different versions:

range(stop) #This assumes it is from the start
range(start, stop) #It defines where to start and where to stop but doesnt include the last number
range(start, stop, step)
Example:

"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function([0,1,2])

