import json
# importing json module

class student_table:       # user table class
    
    def create_student(self):
        # create user method
        student_id = int(input("Enter student id to create: "))                   # taking student id input
        student_name = input("Enter student name : ")                             # taking student name input
        student_company_name = input("Enter student company_name: ")                         # taking student stream input
        student_role = input("Enter student role : ")                             # taking student role input

        file_obj = open('./data/myfirstfile.txt', "rt")       # opening the file
        file_line = file_obj.readline()                                     # reading the lines
        file_obj.close()

        json_obj = json.loads(file_line)                                    # loads for doing operations
        student_data = {"id": student_id,                                         # all user data as dict
                    "name" : student_name,    
                    "company" : student_company_name,
                    "role" : student_role
                    }
        
        json_obj["students"].append(student_data)                                 # append to array of users
        json_str = json.dumps(json_obj)                                     # dumps to json string

        file_obj = open('./data/myfirstfile.txt', "wt")       # then write the file 
        file_obj.write(json_str)
        file_obj.close()

        print("User successfully added")                                    # print the message

    # create_user()

    def get_student(self):
        # get all user info
        file_obj = open('./data/myfirstfile.txt', "rt")       # opening the file
        file_line = file_obj.readline()                                     # reading the lines
        file_obj.close()

        json_obj = json.loads(file_line)                                    # then load to print all the data
        print(json_obj)

    # get_users()

    def update_student(self):
        student_id = int(input("Enter student id to update: "))                   # taking inputss from users
        student_name = input("Enter student name : ")             
        student_company_name = input("Enter student company_name : ")
        student_role = input("Enter student role : ")

        file_obj = open('./data/myfirstfile.txt', "rt")       # opening the user data then read
        file_line = file_obj.readline()
        file_obj.close()

        json_obj = json.loads(file_line)
        
        json_obj["students"][student_id - 1] = {  "id" : student_id,
                                            "name" : student_name,
                                            "company" : student_company_name,
                                            "role" : student_role
                                            }                               # updating the particular data
        json_str = json.dumps(json_obj)

        file_obj = open('./data/myfirstfile.txt', "wt")       # and again write the data into file
        file_obj.write(json_str)
        file_obj.close()

        print("User updated successfully")                                  # printing successful message
        
    # update_user()

    def delete_student(self):                                                  
        # delete user method
        student_id = int(input("Enter user id to delete : "))                  # taking student id input 
        file_obj = open('./data/myfirstfile.txt', "rt")       # opening the file and read
        file_line = file_obj.readline()
        file_obj.close()

        json_obj = json.loads(file_line)                                    # load that file
        
        json_obj["students"].pop(student_id - 1)                                  # deleting the student
        json_str = json.dumps(json_obj)                                     # then dumps to json string

        file_obj = open('./data/myfirstfile.txt', "wt")       # writing to the file
        file_obj.write(json_str)
        file_obj.close()

        print("User deleted successfully")                                  # printing the message

    # delete_user()
        
user1 = student_table()
# user1.create_student()
# user1.get_student()
# user1.update_student()
user1.delete_student()