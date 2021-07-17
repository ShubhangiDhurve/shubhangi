import json
# import requests
 
# # Get dummy data using an API
# res = requests.get("http://dummy.restapiexample.com/api/v1/employees")
 
# # Convert data to dict
# data = json.loads(res.text)
 
# # Convert dict to string
# data = json.dumps(data)
a={
    "name": "David",
    "class": "I",
    "age": 6
}
b=json.loads(a)
print(b)
