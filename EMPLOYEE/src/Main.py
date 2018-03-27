from interpreter_controller import InterpreterController
# from View.graph_view import *
from Model.Interpreter import *
from File_Handler.file_handler import *
from DataValidation.emp_data_validator import *
from Model.Database.Database import *
import sys


if __name__ == '__main__':
    InterpreterController(Interpreter(
                            Database(),
                            FileHandler(),
                            DataValidator(),
                            InterpreterController.set_file_path(sys.argv)
                            )
                        ).cmdloop()

                            # sys.argv is a list in Python, which contains the command-line
                            # arguments passed to the script.
                            # With the len(sys.argv) function you can count the number of arguments.