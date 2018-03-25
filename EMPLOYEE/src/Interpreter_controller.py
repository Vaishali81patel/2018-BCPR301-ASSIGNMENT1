from cmd import Cmd

class Inpreter_Controller(Cmd):

    def __init__(self, emp_view, emp_interpreter):
        Cmd.__init__(self)  # Initialize self
        self.prompt = '> '  # Initialize prompt
        self.my_view = emp_view  # Initialize view
        self.my_interpreter = emp_interpreter # Initialize interpreter

    def do_add (self, *args):
        # This function enable to add employee data into system
        # Which basically give all the available option to the user
        # parse: splits the given sequence of characters or values (text)
        # into smaller parts based on some rules
        #
        # Written By: Patel
        #
        arg_found = False
        options_add_arr = self.parse_args (args)
        option_add_dict = {
            '-l': self.my_interpreter.load_emp_data_file,
            '-m': self.manual_add,
            '-d': self.my_interpreter.load_database
        }
        for key, value in option_add_dict.items ():
            if options_add_arr[0] == key:
                arg_found = True
                if not self.try_launch (key, value, options_add_arr):
                    self.my_view.show ("This Command FAILED")
                else:
                    self.my_view.show ("Command SUCCESS")
        if not arg_found:
            self.my_view.show ("the given command does not with this options ")

