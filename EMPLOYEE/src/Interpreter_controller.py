from cmd import Cmd

class Inpreter_Controller(Cmd):

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
    # Written By: Vaishali Patel
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
                    '-d': self.my_interpreter.save_database,
                    '-s': self.my_interpreter.serialize_data_arr
                    }
        self.find_in_dict (options_arr, option_dict)