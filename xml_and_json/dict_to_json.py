import json

# Define a dictionary
dict_data = { "student_id": "10525", "name": "Madhurendra", "batch": 1, "semester":1 }

# Convert dictionary into json object without indentation
json_data = json.dumps(dict_data)
# print json data
print(json_data)