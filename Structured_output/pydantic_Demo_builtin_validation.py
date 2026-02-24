from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str= 'Don Himkesh Tak'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10,default = 7.36, description='CGPA is the representation of its grades in his acadmics' )
    
new_student = {'age':19,'email':'himkeshtak165@gmail.com'}
# just try diiferent email changes and it will tell
# valid email or not valid email
student = Student(**new_student)
student_dict = dict(new_student)

print(student_dict['age'])
student_json = student.model_dump_json()
print(student)
print(student_json)

