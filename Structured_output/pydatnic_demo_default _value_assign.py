from pydantic import BaseModel

class Student(BaseModel):
    name: str = 'Don Himkesh Tak'
    
new_student = {}
# new_student = {'name': 32} ..........try this too to get ganda error

student = Student(**new_student)

print(student)

