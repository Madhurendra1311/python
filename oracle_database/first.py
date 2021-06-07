import cx_Oracle

class Doctor_Details:
    def create_table(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        #Creating table with a structure
        sql_create="""
        CREATE TABLE DOCTOR_DETAILS(
        DOCTOR_ID NUMBER,
        FIRST_NAME VARCHAR(255),
        LAST_NAME VARCHAR(255),
        AGE NUMBER,
        DEPARTMENT_NAME VARCHAR(255),
        SALARY NUMBER,
        PHONE_NO VARCHAR(255),
        ADDRESS VARCHAR(255))"""
        #executing the create table query
        cursor.execute(sql_create)
        print("Table created successfully")


    def insert_details(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        #Inserting data into table using insert query
        sql_insert="""
            INSERT INTO DOCTOR_DETAILS VALUES(:1, :2, :3, :4, :5, :6, :7, :8)"""

        #Taking user input for inserting details
        ID=int(input("ENTER THE DOCTOR'S ID:"))
        F_NAME=input("ENTER THE FIRST NAME:")
        L_NAME=input("ENTER THE LAST NAME:")
        INPUT_AGE=int(input("ENTER THE AGE OF DOCTOR:"))
        D_NAME=input("ENTER THE DEPARTMENT NAME:")
        SALARY=float(input("ENTER THE SALARY OF DOCTOR:"))
        PHONE=int(input("ENTER THE PHONE NUMBER OF DOCTOR:"))
        PLACE=input("ENTER THE ADDRESS OF THE DOCTOR:")
        details=[(ID,F_NAME,L_NAME,INPUT_AGE,D_NAME,SALARY,PHONE,PLACE)]
        #executing insert  query using executemany
        cursor.executemany(sql_insert,details)
        print("Data inserted successfully")
        conn.commit()
        conn.close()
    
    def select_details(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        #sql query for 
        sql_select="""SELECT * FROM DOCTOR_DETAILS"""
        cursor.execute(sql_select)
        for i in cursor:
            print(i)
        conn.commit()
        conn.close()

    def update_details(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        #sql query for updating details
        sql_update="""UPDATE DOCTOR_DETAILS SET FIRST_NAME=:2,LAST_NAME=:3,AGE=:4,DEPARTMENT_NAME=:5,SALARY= :6,PHONE_NO=:7,ADDRESS=:8 WHERE DOCTOR_ID=:1"""
        ID=int(input("ENTER THE DOCTOR'S ID:"))
        F_NAME=input("ENTER THE FIRST NAME:")
        L_NAME=input("ENTER THE LAST NAME:")
        INPUT_AGE=int(input("ENTER THE AGE OF DOCTOR:"))
        D_NAME=input("ENTER THE DEPARTMENT NAME:")
        SALARY=float(input("ENTER THE SALARY OF DOCTOR:"))
        PHONE=int(input("ENTER THE PHONE NUMBER OF DOCTOR:"))
        PLACE=input("ENTER THE ADDRESS OF THE DOCTOR:")
        updated_details=(F_NAME,L_NAME,INPUT_AGE,D_NAME,SALARY,PHONE,PLACE,ID)
        cursor.execute(sql_update,updated_details)
        print("Data updated succssfully")
        conn.commit()
        conn.close()


    def delete_table(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        #sql query for deleting the table
        sql_deletetable="""DROP TABLE DOCTOR_DETAILS"""
        #execute the sql query
        cursor.execute(sql_deletetable)
        print("Table deleted successfully")
        conn.commit()
        conn.close()

    def delete_allRow(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        # ID1=int(input("ENTER THE ID OF DOCTOR WHICH YOU WANT TO DELETE DETAILS"))
        #sql query for deleting a row from table
        sql_deleteAllRow="""DELETE FROM DOCTOR_DETAILS"""
        cursor.execute(sql_deleteAllRow)
        print("Successfully deleted all the row")
        conn.commit()
        conn.close()

    def delete_row(self):
        #connecting sql to python
        conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
        #cursor starting
        cursor=conn.cursor()
        doc_id=int(input("ENTER THE DOCTOR'S ID:"))
        sql_deleteOneRow="""DELETE FROM DOCTOR_DETAILS WHERE DOCTOR_ID= :DOCTOR_ID"""
        cursor.execute(sql_deleteOneRow,{'DOCTOR_ID':doc_id})
        print("Successfully deleted one row")
        conn.commit()
        conn.close()