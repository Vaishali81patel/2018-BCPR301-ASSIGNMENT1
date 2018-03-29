class Interpreter:
    # This is the model class which handles various modules
    # This interpreter require data_validator, \
    # default file path file handler and database handler
    # In order to handle the system correctly
    #
    # Written by: Patel
    #

    def __init__(self, emp_data_validator, emp_file_handler,
                 emp_file_path, emp_database_handle):
        # Initialize attributes in order to catch modules
        #
        # Hereby; Declare one data_arr_list to catch the employee data
        # so that the data validator is able to validate the data
        #
        self.data_arr_list = []
        self.data_validator = emp_data_validator
        self.my_file_handler = emp_file_handler
        self.default_file_path = emp_file_path
        self.database_handler = emp_database_handle

    def emp_data_arr(self):
        # Initialize the default employee data array in a list
        # written by: Patel
        #
        return self.data_arr_list

    def serialize_emp_data_arr(self, args=''):
        # This function enable to serialize employee data
        # Raise Exception Error if unable to do so
        #
        # Written by: Patel
        # args means for however many arguments you take in, \
        # it will catch them all
        if args == '':
            try:
                self.my_file_handler.shelve_file
                (self.data_arr_list, self.default_file_path)
            except OSError:
                print (OSError)
                return false
            else:
                try:
                    self.my_file_handler.shelve_file(self.data_arr_list, args)
                except OSError:
                    print (OSError)
                    return false

    def save_emp_file(self, args=''):
        # This function enable to save employee data
        # in to the default file or
        # the user can save the employee data in a
        # specified file location once enter the data successfully
        # Raise exception Error if unable to do so
        #
        # Written by: Patel
        # args means for however many arguments you take in, \
        # it will catch them all
        if args == '':
            try:
                self.my_file_handler.save_file
                (self.data_arr_list, self.default_file_path)
            except OSError:
                print (OSError)
                return false
            else:
                try:
                    self.my_file_handler.save_file(self.data_arr_list, args)
                except OSError:
                    print(OSError)
                    return false

    def save_file_into_database(self, database_name='my_db'):
        # This function enable to save data_arr_list in to the database
        # The default database is set until
        # the user states one
        # Raise exception error if unable to do so
        #
        # Written By: Vaishali Patel
        #
        self.database_handler.save_emp_data(self.emp_data_arr, database_name)

    def load_emp_file(self, file_path):
        # This function enable to load data from .csv file
        # cleanse the employee data before bring in to front
        # By the set_emp_data_arr function
        #
        # Written By: Patel
        #
        self.set_emp_data_arr(self.my_file_handler, load_emp_file(file_path))

    def load_emp_database(self, database_name='my_db'):
        # This function enable to bring emp_data_arr to the front
        # cleanse the employee data before bring in to front
        # By the set_emp_data_arr function
        #
        # Written By: Patel
        #
        self.set_emp_data_arr(
                    self.database_handler,
                    get_employee_info(database_name)
                    )

    def manual_data_entry(self, new_employee_data):
        # This function enable user to add manual data in to
        # the .csv or the database directly and
        # append to the existing data records
        #
        # Written By: Patel
        #
        data = self.data_validator.validate_emp_data(new_employee_data)
        self.data_arr_list.append(data)
        return True

    def set_emp_data_arr(self, valid_data_arr):
        # This function enable to create valid_data_arr_list and send to
        # The validate_emp_data function to pass the
        # Validate data test
        # Raise the exception error if unable to pass the valid data test
        #
        # Written By: Patel
        self.data_arr_list = self.data_validator.validate_emp_data(valid_data_arr)
