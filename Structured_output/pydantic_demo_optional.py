from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str= 'Don Himkesh Tak'
    age: Optional[int] = None
    
new_student = {'age':19}
#try 'age' : '19' which makes the age into a string , but still pydantic is able to convert it into the integer back and give the output
# which is basically coercion in pydantic
student = Student(**new_student)

print(student)

