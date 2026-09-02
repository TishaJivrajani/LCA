#to create,append,remove key value pair in dictionary

#creating a dictionary
student = {
             "name"   :  "Tisha Jivrajani",
             "college":  "MIT WPU",
             "course" :  "CSE (AIDS)",
             "cgpa"   :  "8.9"
          }

print("initially created dictionary is:",student)
#appending one key value pair age = 18
student["age"]="18"

print("new dict with appended key value pair is",student)
#delecting one key value pair from dictionary 
student.pop("course")

print("new dict with appended key value pair and deleted key value pair is:",student)