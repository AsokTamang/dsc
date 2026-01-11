import json
#json.load() is used for reading the json data from a file in the python dict format
#json.loads() is used for reading the json data which is in string format into python dict
#json.dump() is used for writing the python dict as json data to a file
#json.dumps() is used for converting the python dict into json string
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

print(json.dumps(random_data,indent = 4))  #here json.dumps() is used to convert the python dict into json string

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

#json.dump() writing python dict into a file as json
#json.dumps()  converting python dict into json data string
#json.load() reading json data from a file in python dict
#json.loads()  reading json string data as python dict