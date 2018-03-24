from cmd import Cmd


class InterpreterController(Cmd):
    # This class is a controller class which enable interpreter (model) and
    # View (Console View) to interconnect with each other and
    # This class also defined command loop enables the associate commands invoke
    #
    # Written By: Patel
    #
    def __init__(self, emp_view, emp_interpreter):
        Cmd.__init__(self)  # Initialize cmd interface here
        self.prompt = '> '  # Initialize prompt
        self.my_view = emp_view  # Initialize view
        self.my_interpreter = emp_interpreter # Initialize interpreter


    @staticmethod
    def set_file_path(self, file_path_args):
        # This function allows the user to set file path for
        # for their file to store or otherwise stay default
        # if not stated by the user
        #
        # Written By: Patel
        #
        if len (file_path_args) > 2:
            print ("too many arguments provided!")
            return file_path_args[0]
        try:
            open (file_path_args[1], 'r')
            return file_path_args[1]
        except OSError as error:
            print (error)
            print ("Defaulting working directory!")
            return file_path_args[0]
        except IndexError:
            print ("default path does not provided!")
            print ("Defaulting working directory!")
            return file_path_args[0]


    def do_add (self, *args):
        # This function enable to add employee data into system
        # Which basically give all the available option to the user
        # parse: splits the given sequence of characters or values (text)
        # into smaller parts based on some rules
        #
        # Written By: Patel
        #
        """*** OPTIONS
                    -l : This option loads the employee information from a file. The file is given to the command as a string.
                    -m : This option does manual data entry. The user will be prompted for step by step employee information to be entered into the system.
                    -d : This option loads the employee information into the system from a database.
                    ***"""
        options_arr = self.parse_args (args)
        option_dict = {
                        '-l': self.my_interpreter.load_emp_file,
                        '-m': self.manual_data_entry,
                        '-d': self.my_interpreter.load_emp_database
                    }
        self.find_in_dict (options_arr, option_dict)


    def do_save (self, *args):
        # This function enable to access dict option for respective file
        # to be stored in the system
        # Raise Exception error if unable to do so
        #
        # Written By: Patel
        #
        """*** OPTIONS
                        -s : This option is a standard save. The information is saved to a file in the existing program files.
                        -d : This option saves the current employee information to the database.
                        -f : This option saves a file to the specific file location.
                    ***"""
        options_arr = self.parse_args (args)
        option_dict = {
                    '-f': self.my_interpreter.save_emp_file,
                    '-d': self.my_interpreter.save_file_into_database,
                    '-s': self.my_interpreter.serialize_emp_data_arr
                    }
        self.find_in_dict (options_arr, option_dict)


    def do_show (self, *args):
        # This function enable to create dictionary option
        # to respective commands and the system find matches
        # to the respective option to show individual map / view
        #
        # Written By: Patel
        #
        """*** OPTIONS
                    -a : This option shows a bar graph of the total sales made by males verse the total sales made by female.
                    -b : This option shows a pie chart of the percentage of female workers verse male workers
                    -c : This option shows a scatter plot graph of peoples age verse their salary.
                    -d : This option shows a pie chart of the BMI of a set of people.
        ***"""
        options_arr = self.parse_args (args)
        option_dict = {
                    '-a': self.my_view.sales_by_gender_graph,
                    '-b': self.my_view.employees_by_gender_graph,
                    '-c': self.my_view.age_verse_salary_graph,
                    '-d': self.my_view.bmi_pie_graph
                }
        for key, value in option_dict.items ():
            if options_arr[0] == key:
                value (self.my_interpreter.emp_data_arr())


    @staticmethod
    def do_quit (args):
        # This function enable to call do_quit()
        # This function terminate the programme
        # When the user enter 'q'
        #
        # Written By: Patel
        #
        do_q = do_quit


    @staticmethod
    def do_manual_emp_data_entry(self):
        # This function enable to invoke manual emp data add function
        # Then passes that information into the manual data in the model
        #
        # Written By: Patel
        #
        self.my_interpreter.manual_data_entry(self,my_view.manual_emp_data_flow())


    @staticmethod
    def find_in_dict_arr(self, options_arr, option_dict):
        # This function enable to match given option to be matched with
        # the option array and option dictionary arrays used in earlier
        # function and try to match with the given option and invoke the
        # particular function to match with that option
        #
        # Written By: Patel
        #
        arg_found = False
        for key, value in options_dict.items ():
            if options_arr[0] == key:
                if not self.try_launch (key, value, options_arr):
                    return
                else:
                    return
        if not arg_found:
            return


    @staticmethod
    def launch_match_option(self, key, value, options_arr):
        # This function enable to invoke the options array and
        # option dictionary and match with the given option and
        # invoke the function which match with it
        #
        # Written By: Patel
        #
        if key == '-m':
            value ()
            return True
        else:
            if len (options_arr) == 2:
                value (options_arr[1])
                return True
            else:
                return False


    @staticmethod
    def parse_args(arg_string):
        # This function enable to parse (break) the string arguments
        # in to the smallest option and try to match with the
        # option array value to invoke particular function match with it
        #
        # Written By: Patel
        #
        try:
            args_arr = None
            for arg in arg_string:
                args_arr = arg.split (' ')
            if len (args_arr) > 2:
                return "Too many arguments supplied!!"
            else:
                return args_arr
        except IndexError:
            return False