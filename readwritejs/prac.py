import json
random_data = {
  "users": [
    {
      "id": 101,
      "name": "Ava Patel",
      "email": "ava.patel@example.com",
      "age": 24,
      "skills": ["Python", "SQL", "Pandas"],
      "is_active": True
    },
    {
      "id": 102,
      "name": "Liam Chen",
      "email": "liam.chen@example.com",
      "age": 28,
      "skills": ["JavaScript", "React", "Node.js"],
      "is_active": False
    },
    {
      "id": 103,
      "name": "Noah Smith",
      "email": "noah.smith@example.com",
      "age": 22,
      "skills": ["Python", "Machine Learning"],
      "is_active": True
    }
  ],
  "company": {
    "name": "TechNova",
    "location": "Toronto",
    "founded": 2018
  }
}

json_string = '''
{
  "users": [
    {
      "id": 301,
      "name": "Oliver Wang",
      "email": "oliver.wang@example.com",
      "age": 27,
      "skills": ["Python", "FastAPI", "MongoDB"],
      "is_active": true
    },
    {
      "id": 302,
      "name": "Emma Wilson",
      "email": "emma.wilson@example.com",
      "age": 24,
      "skills": ["SQL", "Power BI", "Excel"],
      "is_active": false
    },
    {
      "id": 303,
      "name": "Lucas Garcia",
      "email": "lucas.garcia@example.com",
      "age": 29,
      "skills": ["JavaScript", "React", "TypeScript"],
      "is_active": true
    }
  ],
  "company": {
    "name": "InsightLabs",
    "location": "Toronto",
    "founded": 2019
  }
}
'''


a =json.loads(json_string)  #here we are converting the json string into python dict
print(a)

with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'w') as f:
    json.dump(random_data,f,indent = 4 )  #here we are writing the JSON data in the given file using json.dump()
    print('json data converted and written into change.txt file')