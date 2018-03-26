from interpreter_controller import InterpreterController
# from View.graph_view import *
from Model.Interpreter import *
# from Model.FileHandler.file_handler import *
# from DataValidation.DataValidator import *
from Model.Database.Database import *
import sys


if __name__ == '__main__':
    InterpreterController(Interpreter(
                            Database(),
                            InterpreterController.set_file_path(sys.argv)
                            )
                          ).cmdloop()
