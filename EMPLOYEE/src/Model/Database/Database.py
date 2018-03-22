from IDatabase import IDatabase
import sqlite3
# This class enable to handle database connection
#
# Author: Patel
#
#
#
class Database:

    def __init__(self):
        # Create an connection object to connect to Employee Database
        self.db_conn = sqlite3.connect('Employee.db')
        # Create a "cursor" variable and cursor object in order to execute the sql command
        self.cursor = None

    def create_db_connection(self,db_conn):
        #
        # This function enable to handle database connection
        # Raise runtime error and type error if unable to connect database
        #
        # Author: Patel
        #
        try:
            self.db_conn = sqlite3.connect(db_conn)   # Try to connect the employee database
            self.cursor = self.db_conn.cursor()  # Try to execute the connection with the employee database
            self.create_table() # try to create the employee table
            return False
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)

    def create_employee_table(self):
        # This function is enable to create employee table
        # Raise runtime error and type error if unable to create employee table
        #
        # Author: Patel
        #
        # Create employee table if not exists
        try:
            create_table = """ 
                            CREATE TABLE IF NOT EXISTS EMPLOYEE (employeeID VARCHAR (6), gender CHAR, age INTEGER,
                            sales INTEGER, bmi VARCHAR(15), salary INTEGER, birthday DATE) 
                            """

            self.cursor.execute (create_table)
            self.db_conn.commit ()
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)


    def insert_employee_data(self, data_arr):
        # This is function is enable to insert employee data into employee table
        # raise runtime error and type error if unable to insert employee data
        #
        # Author: Patel
        #
        #
        try:
            for employee in data_arr:   # Retrieve employee data in to data_arr "array" format
                insert_string ="""
                                INSERT INTO EMPLOYEE(employeeID, gender, age, sales, bmi, salary, birthday)
                                VALUES ("{employeeID}","{gender}","{age}","{sales}","{bmi}","{salary}","{birthday}");                                    
                                """

                insert_values = insert_string.format(employeeID = employee[0],
                                                      gender = employee[1],
                                                      age = employee[2],
                                                      sales = employee[3],
                                                      bmi = employee[4],
                                                      salary = employee[5],
                                                      birthday = employee[6])
                self.cursor.execute (insert_values)
                self.db_conn.commit ()
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)


    def select_employee_data(self):
        # This function is unable to fetch employee data from employee table
        # Raise runtime error and type error if unable to retrive data from employee table
        #
        # Author: Vaishali Patel
        #
        #
        dara_arr = [] # Retrieve employee data in dara_arr array format
        try:
            for employee in data_arr:  # Retrieve employee data in to data_arr "array" format
                select_values="""
                              SELECT * FROM EMPLOYEE
                              """
                self.cursor.execute(select_values) # Execute the SQL Command
                self.db.conn.commit()              # Commit the changes in Database
                results = cursor.fetchall ()
                for row in results:
                    employeeID = raw[0],
                    gender = raw[1],
                    age = raw[2],
                    sales = raw[3],
                    bmi = raw[4],
                    salary = raw[5],
                    birthday = raw[6]
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)
        finally:
            print(FileNotFoundError)
