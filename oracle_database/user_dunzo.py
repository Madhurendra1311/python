import cx_Oracle

#connecting sql to python
conn=cx_Oracle.connect('kmadhu1311/pass//localhost:1521/xe')
#cursor starting
cursor=conn.cursor()

class Dunzo:
    def dunzo_table(self):
        #Creating table with a structure
        sql_create="""
        CREATE TABLE DUNZO_DETAILS(
        DUNZO_ID NUMBER,
        name VARCHAR(255),
        email VARCHAR(255),
        mobile NUMBER,
        address: [{ street VARCHAR(255),landmark VARCHAR(255),actual_map_address VARCHAR(255),longitude NUMBER,latitude NUMBER, contact_person VARCHAR(255),contact_detail: NUMBER,address_type: VARCHAR(255)}]
        latitude NUMBER,
        avatar VARCHAR(255),
        food_type VARCHAR(255),
        distance VARCHAR(255),
        place VARCHAR(255),
        delivery_time VARCHAR(255)
        food_category VARCHAR(255)
        food_items: [{ item_name VARCHAR(255),item_price NUMBER,catagory_food: VARCHAR(255)},{ item_name VARCHAR(255),item_price NUMBER,catagory_food: VARCHAR(255)}] )"""
        #executing the create table query
        cursor.execute(sql_create)
        print("Table created successfully")