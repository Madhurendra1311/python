# import json

# def insert_student():
#     user_input1 = raw_input("Enter the new student id: ")
#     user_input2 = raw_input("Enter the new student name: ")
#     user_input3 = raw_input("Enter the new student stream: ")
#     file_obj = open('./data/myfirstfile.txt', 'rt')
#     file_line = file_obj.readline()
#     file_obj.close()

#     json_obj = json.loads(file_line)
#     json_obj["students"].append(user_input1)
#     json_obj["students"].append(user_input2)
#     json_obj["students"].append(user_input3)
#     json_str = json.dumps(json_obj)

#     file_obj = open('./data/myfirstfile.txt', 'wt')
#     file_obj.write(json_str)
#     file_obj.close()

#     print("Added one more student id" +  user_input1)
#     print("Added one more student name" + user_input2)
#     print("Added one more student stream" + user_input3)

# insert_student()

# # def read_student():