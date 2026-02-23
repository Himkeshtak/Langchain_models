from typing import TypedDict

class candidate(TypedDict):
    {
        "name": str,
        "age": int,
        "skills": list[str]
    }
    
new_candidate: candidate = {"name": "Don Tak",
                            "age": 19,
                            "skills": ["C", "C++", " Deep learning"]
                            }

print (new_candidate)