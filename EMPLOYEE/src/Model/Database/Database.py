# from IDatabase import IDatabase
import sqlite3
# This class enable to handle database connection
#
# Author: Patel
#


class Database:

    def __init__(self):
        # Create an connection object to connect to Employee Database
        self.db_conn = sqlite3.connect('Employee.db')
        # Create a "cursor" variable and cursor object
        # in order to execute the sql command
        self.cursor = None

    def create_db_connection(self, db_conn):
        #
        # This function enable to handle database connection
        # Raise runtime error and type error if unable to connect database
        #
        # Author: Patel
        #
        try:
            self.db_conn = sqlite3.connect(db_conn)
            # Try to connect the employee database
            self.cursor = self.db_conn.cursor()
            # Try to execute the connection with the employee database
            self.create_table()
            # try to create the employee table
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
            create_table = """ CREATE TABLE IF NOT EXISTS EMPLOYEE \
                                (employeeID VARCHAR (6), gender CHAR, \
                                age INTEGER, sales INTEGER, \
                                salary INTEGER, birthday DATE)"""
            self.cursor.execute(create_table)
            self.db_conn.commit()
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print (TypeError)

    def insert_employee_data(self, data_arr_list):
        # This is function is enable to insert data into employee table
        # raise runtime error and type error if unable to insert data
        #
        # Author: Patel
        #
        #
        try:
            for employee in data_arr_list:
                # Retrieve employee data in to data_arr "array" format
                insert_string = """
                                INSERT INTO EMPLOYEE(
                                employeeID, gender, age, sales, \
                                bmi, salary, birthday)
                                VALUES ("
                                {employeeID}" , "{gender}" , \
                                "{age}" , "{sales}" , \
                                "{bmi}" , "{salary}" , "{birthday}" ); \                                 
                                """

                insert_values = insert_string.format(
                                                  employeeID=employee[0],
                                                  gender=employee[1],
                                                  age=employee[2],
                                                  sales=employee[3],
                                                  bmi=employee[4],
                                                  salary=employee[5],
                                                  birthday=employee[6])
                self.cursor.execute(insert_values)
                self.db_conn.commit()
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print(TypeError)

    def select_employee_data(self):
        # This function is unable to retrieve \
        # data_arr_list from employee table
        # Raise runtime error and type error \
        # if unable to retrieve data from employee table
        #
        # Author: Patel
        #
        data_arr_list = []  # Retrieve employee data in dara_arr list format
        try:
            for employee in data_arr_list:
                    # Retrieve employee data in to data_arr "array" format
                select_values = """
                              SELECT * FROM EMPLOYEE
                              """
                self.cursor.execute(select_values)  # Execute the SQL Command
                self.db.conn.commit()  # Commit the changes in Database
                results = cursor.fetchall()
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
            print(TypeError)
        finally:
            print(FileNotFoundError)

    def save_employee_data(self, data_arr_list, database_name='db_name'):
        #
        # This function is unable to \
        # save employee data into employee.db
        # Raise runtime error and type error \
        # if unable to retrieve database file
        #
        # Author: Patel
        #
        self.create_db_connection(db_conn)
        try:
            if self.insert_employee_data(data_arr_list):
                return True
            else:
                return False
        except OSError:
            print("cannot open")

    def turn_emp_data_into_info(self, database_name):
        #
        # This function is unable to turn \
        # employee data into information and then
        # Raise runtime error and type error \
        # if unable to retrieve database file \
        #
        # Author: Patel
        #
        try:
            self.create_db_connection(database_name)
            return self.format.incoming_data_into_info(
                            self, select_employee_data())
        except ConnectionError:
            print(ConnectionError)
        except TypeError as error:
            print(TypeError)

    def format_employee_data(self, emp_raw_arr):
        #
        # This function is unable to retrieve \
        # employee data from employee database and then
        # Format into arrays of array in order \
        # to validate the employee data
        # Raise runtime error and type error \
        # if unable to retrieve database file
        #
        # Author: Patel
        #
        employee_data_arr = []  # Declare temp list  array
        # Declare list data type for employee \
        # data to be retrieve in format
        try:
            for list in emp_raw_arr:
            data_arr_list = []
            try:
                    for data in list:
                        data_arr_list.append(data)
                    employee_data_arr.append(data_arr_list)
            except TypeError as OOPS:
                print(OOPS)
            return employee_data_arr
        except ValueError:
            print("data format mismatch")

